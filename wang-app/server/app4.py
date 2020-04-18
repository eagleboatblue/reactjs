from flask import Flask, jsonify, request
import json

f = open('books.json')
BOOKS = json.load(f)

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
    response_object['books'] = BOOKS
    return jsonify(response_object)
    
if __name__ == '__main__':
  app.run(host="localhost", port=5000)