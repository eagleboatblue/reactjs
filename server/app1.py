from flask import Flask, request

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/ping', methods=['GET'])
def ping_pong():
    return 'pong!'

app.run()