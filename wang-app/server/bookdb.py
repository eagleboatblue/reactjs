from pymongo import MongoClient
from bson.objectid import ObjectId
import json

def getBookDB():
    client = MongoClient('mongodb://localhost:27017')
    db = client['test-database']
    books = db.books
    return books

all_books = [
    {
        "id": "12345",
        "title": "On the Road",
        "author": "Jack Kerouac",
        "read": True,
        "price": 19.99,
        "rating": 3
    },
    {
        "id": "67890",
        "title": "Harry Potter and the Philosopher's Stone",
        "author": "J. K. Rowling",
        "read": False,
        "price": 9.99,
        "rating": 5
    },
    {
        "id": "23456",
        "title": "Green Eggs and Ham",
        "author": "Dr. Seuss",
        "read": True,
        "price": 4.99,
        "rating": 1
    }
]

def addBooks(all_books):
    books = getBookDB()
    results = books.insert_many(all_books)
    for id in results.inserted_ids:
        print("Books Added. The course Id is", str(id))

def getBooks():
    books = getBookDB()
    result = books.find()
    bookList = []
    for book in result:
        book.pop('_id',None)
        bookList.append(book)
    return bookList

def test():
    books = getBooks()
    print(books)
    # for book in books:
    #     print("book found with id =", book['id'])

#test()
#addBooks(all_books)
