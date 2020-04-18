# Python /books server

## to start the server
```bash
ce server
source stripe/bin/activate
python app.py
```
[Get books in json format](http://localhost:5000/books)

[ping/pang](http://localhost:5000/ping)

## Configure host and port
By default, the Flask application is executed in

host = localhost
port = 5000

to change them, edit the app.py as
```js
app.run (host = "10.100.100.10", port = 9566)

if __name__ == '__main__':
  app.run(port=9566)
```