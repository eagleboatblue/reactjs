from pymongo import MongoClient
from bson.objectid import ObjectId
import json
import uuid

def getBookDB():
    client = MongoClient('mongodb://localhost:27017')
    db = client['test-database']
    bookdb = db.books
    return bookdb

def getBooks():
    bookdb = getBookDB()
    result = bookdb.find()
    bookList = []
    for book in result:
        book.pop('_id',None)
        bookList.append(book)
    return bookList

all_books = [
    {
        "_id": uuid.uuid4().hex,
        "title": "On the Road",
        "author": "Jack Kerouac",
        "read": True,
        "price": 19.99,
        "rating": 3
    },
    {
        "_id": uuid.uuid4().hex,
        "title": "Harry Potter and the Philosopher's Stone",
        "author": "J. K. Rowling",
        "read": False,
        "price": 9.99,
        "rating": 5
    },
    {
        "_id": uuid.uuid4().hex,
        "title": "Green Eggs and Ham",
        "author": "Dr. Seuss",
        "read": True,
        "price": 4.99,
        "rating": 1
    }
]

def create(book):
    db = getBookDB()
    result = db.insert_one(book)
    return result.inserted_id
    
def delete(book_id):
    db = getBookDB()
    result = db.find_one_and_delete({'_id':book_id})
    return book_id
    
def addBooks(all_books):
    books = getBookDB()
    results = books.insert_many(all_books)
    for id in results.inserted_ids:
        print("Books Added. The course Id is", str(id))


#   if __name__ == '__main__':
    # books = getBooks()
    # for book in books:
    #     print(book)
    #     print("book found with id =", book['id'])

addBooks(all_books)
