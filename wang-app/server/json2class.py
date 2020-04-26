import json
from book import *

f = open('books.json')

data = json.load(f)
books = []
for i in data:
    books.append(book(i))

for i in books:
     print(i)   

# total = totalPrice(books)
# print("Total price is $%f" %total)
f.close()
