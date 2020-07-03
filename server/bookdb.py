"""
BookDB class provide all CRUD database access.
"""
from pymongo import MongoClient
import json
import uuid

class BookDB:
    """
    Implementation of CRUD for Book class
    """
    def __init__(self,dbname,url):
        self.dbname = dbname
        self.url = url

    def getBookDB(self):
        client = MongoClient(self.url)
        db = client[self.dbname]
        bookdb = db.books
        return bookdb

    def getBooks(self):
        bookdb = self.getBookDB()
        result = bookdb.find()
        bookList = []
        for book in result:
            bookList.append(book)
        return bookList

    # Create
    def create(self, book):
        """
        Create a book in database
        """
        db = self.getBookDB()
        result = db.insert_one(book)
        return result.inserted_id

    # Retrieve
    def getBook(self, _id):
        """
        Retrieve a book from database by _id
        """
        db = self.getBookDB()
        result = db.find_one({'_id':_id})
        return result

    # Update
    def update(self, _id, book):
        """
        Update one record in database
        """
        book["_id"] = _id
        self.delete(_id)
        self.create(book)

    # Delete
    def delete(self, book_id):
        """
        Delete a book by _id
        """
        db = self.getBookDB()
        result = db.find_one_and_delete({'_id':book_id})
        return book_id
        
    def addBooks(self, all_books):
        bookdb = self.getBookDB()
        results = bookdb.insert_many(all_books)
        for id in results.inserted_ids:
            print("Books Added. The course Id is", str(id))


if __name__ == '__main__':
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
    db = BookDB('mydb','mongodb://localhost:27017')
    # insert initial book sets
    # db.addBooks(all_books)
    # get all books from mongodb
    books = db.getBooks()
    for book in books:
        print(book)
    # book = db.getBook("5ee95435aebd4e3da5b95b17")
    # book["price"]=100.99
    # db.update(book)
    # print(book)