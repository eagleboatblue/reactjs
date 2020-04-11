import React, { useEffect, useState } from 'react';
import './App.css';
import * as ReactBootStrape from 'react-bootstrap';

function App() {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    fetch('/books').then(response => 
      response.json().then(data => {
      setBooks(data.books);
    }))
  }, []);

  const renderBook = (book, id) =>{
    return(
      <tr align="left" key={id}>
        <td>{book.title}</td>
        <td>${book.price}</td>
      </tr>
    )
  };

  return (
    <div className="App">
    <font color="darkblue" size="3">Book List</font>
      <ReactBootStrape.Table striped bordered hover>
        <thead>
          <th bgcolor="lightblue">Title</th>
          <th bgcolor="lightblue">Price</th>
        </thead>
        <tbody>
          {books.map(renderBook)}
        </tbody>
      </ReactBootStrape.Table>
    </div>
  );
}

export default App;
