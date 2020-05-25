#import uuid
from flask import Flask, jsonify, request


BOOKS = [
    {
        '_id': '12345',
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True,
        'price': '19.99'
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
#DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return '<html><body><h1>pong!</h1></body></html>'


@app.route('/books', methods=['GET'])
def all_books():
    response_object = {'status': 'success'}
    response_object['books'] = BOOKS
    return jsonify(response_object)

if __name__ == "__main__":
    app.debug = True
    app.run()