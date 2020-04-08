import React, { useEffect, useState } from 'react';
import './App.css';
import {Books} from "./components/Books";

function App() {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    fetch('/books').then(response => 
      response.json().then(data => {
      setBooks(data.books);
    }))
  }, []);
  return (
    <div className="App">
      <Books books={books}/>
    </div>
  );
}

export default App;
