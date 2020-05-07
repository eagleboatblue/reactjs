from book2 import *
from bookdb import *

bookList = getBooks()
bookObjects = []
for b in bookList:
    bookObjects.append(book(b))

for book1 in bookObjects:
     print(book1)   

print("Total price is $%5.2f" %totalPrice(bookObjects))