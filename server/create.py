"""
insert a sample book to MongoDB
"""
from pymongo import MongoClient
import uuid

book = {
    "_id": uuid.uuid4().hex,
    "title": "White Fragility: Why It's So Hard for White People to Talk About Racism",
    "author": "Robin DiAngelo",
    "read": False,
    "price": 11.69,
    "rating": 5
}

client = MongoClient('mongodb://localhost:27017')
db = client['mydb']
bookdb = db.books

result = bookdb.insert_one(book)
print(result.inserted_id)