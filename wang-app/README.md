# Create React App implement CRUD for books stored in MongoDB

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## To Start this appliction
```
npm start
```
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

## Application File Structures
* public > index.html (Application Title; <div id="root">)
* src/index.js > src/Main/index.js > src/App.js > src/components/BookManager
* BookManager > Uses (AddBookForm; EditBookForm; BookTable)
* src/forms/AddBookForm
* src/forms/EditBookForm
* src/tables/BookTable

## Functionalities
File | Function
|---|---|
BookManager  | Main page for list book; add new book; edit existing book; delete book
BookTable    | Display book list
EditBookForm | Edit existing book form
AddBookForm  | Add new book form



## Dependencies 
* axios
```
npm install axios
```
### `npm run build`

Builds the app for production to the `build` folder.<br />
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.<br />
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

