from flask import Flask, jsonify, request
import json
import bookdb

# def getBooks():
#     f = open('books.json')
#     books = json.load(f)
#     return books

#BOOKS = bookdb.getBooks()

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
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