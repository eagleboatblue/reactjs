
##
1. Call Python server (http://localhost:5000/books) 
```json
   "proxy": "http://localhost:5000" in package.json.
```
2. Read data from MongoDB in Python server.  
```py
fetch('/books').then(response => 
      response.json().then(data => {
      setBooks(data.books);
      }))
```
3. Map data to UI model.
```

```

4. Display data.
```

```
