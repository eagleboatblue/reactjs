import math
import numpy as np
import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
from matplotlib import style

# Adjusting the size of matplotlib
import matplotlib as mpl

# First,  insert the following imports for our Scikit-Learn:
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor

from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split


start = datetime.datetime(2015, 1, 1)
end = datetime.datetime(2020, 7, 11)
#end = datetime.datetime(2020, 7, 20)
#end = datetime.datetime(2020, 7, 23)

df = web.DataReader("AAPL", 'yahoo', start, end)
print(df.head())
print(df.tail())
#----------------------------------------------------------------------------

#The Moving Average makes the line smooth 
#and showcase the increasing or decreasing trend of stocks price.
#Let’s start code out the Rolling Mean (Moving Average) — to determine trend
close_px = df['Adj Close']
mavg = close_px.rolling(window=20).mean().shift(-10)
#print(mavg)

mpl.rc('figure', figsize=(8, 7))
mpl.__version__

# Adjusting the style of matplotlib
style.use('ggplot')

close_px.plot(label='AAPL')
mavg.plot(label='mavg')
plt.legend()
plt.show()
#---------------------------------------------------------------------------

#Return Deviation - to determine risk and return
#Logically, our ideal stocks should return as high and stable as possible
rets = close_px / close_px.shift(1) - 1
rets.plot(label='return')
plt.legend()
plt.show()

#-------------------------------------------------------------------------
# Analysing your Competitors Stocks
# assume we are interested in technology companies and want to compare the big guns: 
# Apple, GE, Google, IBM, and Microsoft.

dfcomp = web.DataReader(['AAPL', 'GE', 'GOOG', 'IBM', 'MSFT'],'yahoo',start=start,end=end)['Adj Close']
print(dfcomp.tail())

#Correlation Analysis — Does one competitor affect others?
#We can analyse the competition by running the percentage change 
# and correlation function in Pandas. Percentage change will find 
# how much the price changes compared to the previous day which defines returns.

retscomp = dfcomp.pct_change()
corr = retscomp.corr()
print(corr)

#Let’s plot Apple and MSFT with ScatterPlot to view their return distributions.
plt.scatter(retscomp.AAPL, retscomp.MSFT)
plt.xlabel('Returns AAPL')
plt.ylabel('Returns MSFT')
plt.show()
# we can see positive correlations among MSFT returns and Apple returns

#At the diagonal point, we will run Kernel Density Estimate (KDE). 
# KDE is a fundamental data smoothing problem where inferences about the population are made, 
# based on a finite data sample. It helps generate estimations of the overall distributions.
#pd.scatter_matrix(retscomp, diagonal='kde', figsize=(10, 10));

#To prove the positive correlations, we will use heat maps to visualize the correlation ranges 
# among the competing stocks. Notice that the lighter the color, 
# the more correlated the two stocks are
plt.imshow(corr, cmap='hot', interpolation='none')
plt.colorbar()
plt.xticks(range(len(corr)), corr.columns)
plt.yticks(range(len(corr)), corr.columns);
plt.show()

#Stocks Returns Rate and Risk
#we also analyse each stock’s risks and returns. 
# In this case we are extracting the average of returns (Return Rate) 
# and the standard deviation of returns (Risk)
plt.scatter(retscomp.mean(), retscomp.std())
plt.xlabel('Expected returns')
plt.ylabel('Risk')
for label, x, y in zip(retscomp.columns, retscomp.mean(), retscomp.std()):
    plt.annotate(
        label, 
        xy = (x, y), xytext = (20, -20),
        textcoords = 'offset points', ha = 'right', va = 'bottom',
        bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))

plt.show()        

## Predicting Stocks Price
# We will use these three machine learning models to predict our stocks:
# Simple Linear Analysis, Quadratic Discriminant Analysis (QDA), and K Nearest Neighbor (KNN)

#First, let's engineer some features: High Low Percentage and Percentage Change.
dfreg = df.loc[:,['Adj Close','Volume']]
dfreg['HL_PCT'] = (df['High'] - df['Low']) / df['Close'] * 100.0
dfreg['PCT_change'] = (df['Close'] - df['Open']) / df['Open'] * 100.0
print(dfreg)

# We will clean up and process the data using the following steps before putting them 
# into the prediction models:
# 1. Drop missing value
dfreg.fillna(value=-99999, inplace=True)
# 2.1  We want to separate 1 percent of the data to forecast
forecast_out = int(math.ceil(0.01 * len(dfreg)))
# 2.2 Separating the label here, we want to predict the AdjClose
forecast_col = 'Adj Close'
dfreg['label'] = dfreg[forecast_col].shift(-forecast_out)
X = np.array(dfreg.drop(['label'], 1))
# 3. Scale the X so that everyone can have the same distribution for linear regression
#X = preprocessing.scale(X)
X = scale(X)
# 4. Finally We want to find Data Series of late X and early X (train) for 
# model generation and evaluation
X_lately = X[-forecast_out:]
X = X[:-forecast_out]
# 5. Separate label and identify it as y
y = np.array(dfreg['label'])
y = y[:-forecast_out]

#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1)
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 50)
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 50)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.5, random_state = 10)


##Model Generation — Where the prediction fun starts

# We will plug and play the existing Scikit-Learn library and 
# train the model by selecting our X and y train sets. 
# Linear regression 线性回归
clfreg = LinearRegression(n_jobs=-1)
clfreg.fit(X_train, y_train)
# Quadratic Regression 2 二次回归
clfpoly2 = make_pipeline(PolynomialFeatures(2), Ridge())
clfpoly2.fit(X_train, y_train)
# Quadratic Regression 3
clfpoly3 = make_pipeline(PolynomialFeatures(3), Ridge())
clfpoly3.fit(X_train, y_train)
# KNN Regression
clfknn = KNeighborsRegressor(n_neighbors=2)
clfknn.fit(X_train, y_train)

##Evaluation
#A simple quick and dirty way to evaluate is to use the score method in each trained model. 
#The score method finds the mean accuracy of self.predict(X) with y of the test data set.
confidencereg = clfreg.score(X_test, y_test)
confidencepoly2 = clfpoly2.score(X_test, y_test)
confidencepoly3 = clfpoly3.score(X_test, y_test)
confidenceknn = clfknn.score(X_test, y_test)

print('The linear regression confidence is ', confidencereg)
print('The quadratic regression 2 confidence is ', confidencepoly2)
print('The quadratic regression 3 confidence is ', confidencepoly3)
print('The knn regression confidence is ', confidenceknn )

# For sanity testing, let us print some of the stocks forecast.

#forecast_set = clf.predict(X_lately)
#forecast_set = clfreg.predict(X_lately)
forecast_set = clfpoly2.predict(X_lately)
#forecast_set = clfpoly3.predict(X_lately)
dfreg['Forecast'] = np.nan
print(dfreg['Forecast'].tail())

#Plotting the Prediction
#visualize the plot with our existing historical data. 
last_date = dfreg.iloc[-1].name
last_unix = last_date
next_unix = last_unix + datetime.timedelta(days=1)

for i in forecast_set:
    next_date = next_unix
    next_unix += datetime.timedelta(days=1)
    dfreg.loc[next_date] = [np.nan for _ in range(len(dfreg.columns)-1)]+[i]
dfreg['Adj Close'].tail(500).plot()
dfreg['Forecast'].tail(500).plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
