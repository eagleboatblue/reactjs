from flask import Flask, jsonify, request
import json
from flask_cors import CORS
import bookdb 

BOOKS = [
    {
        '_id': '12345',
        'title': 'On the Road',
        'author': "Jack's Kerouac",
        'read': True,
        'price': 19.99
    },
    {
        '_id':'23456',
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False,
        'price': '9.99'      
    },
    {
        '_id': '34567',
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True,
        'price': '4.99'
    }
]

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
CORS(app)
app.config.from_object(__name__)

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/books', methods=['GET'])
def all_books():
    response_object = {'status': 'success'}
    books = bookdb.getBooks()
    print(books)
    response_object['books'] = books
    return jsonify(response_object)
    
if __name__ == '__main__':
    app.run(host="localhost", port=5000)