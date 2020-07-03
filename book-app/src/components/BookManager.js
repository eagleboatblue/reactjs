import React, { useState, Fragment, useEffect } from 'react'
import axios from 'axios'
import AddBookForm from './forms/AddBookForm'
import EditBookForm from './forms/EditBookForm'
import BookTable from './tables/BookTable'
import Popup from './Popup'

const BookManager = () => {
	// Data
	const booksData = []
	const initialFormState = { _id: null, title: '', author: '', price: '' , read:false, rating:0}

	// Setting state
	const [ books, setBooks ] = useState(booksData)
	const [ currentBook, setCurrentBook ] = useState(initialFormState)
	const [ editing, setEditing ] = useState(false)

	useEffect(() => {
		fetch('http://localhost:5000/books').then(response => 
		  response.json().then(data => {
		  setBooks(data.books);
		}))
	  }, []);

	function getBooks() {
		fetch('http://localhost:5000/books').then(response => 
		  response.json().then(data => {
		  setBooks(data.books);
		}))	;	
	}
	  
	// CRUD operations
	const addBook = book => {
		// book.id = books.length + 1
		// setBooks([ ...books, book ])
		console.log("add: " + book)
        axios.post("http://localhost:5000/books", book)
            .then(response => {
				console.log(response)
				getBooks()
            })
            .catch(error => {
                console.log(error)
			})
	}

	const deleteBook = _id => {
		setEditing(false)
		console.log("deleteBook: " + _id)
        axios.delete("http://localhost:5000/books/" + _id)
            .then(response => {
				console.log(response)
				getBooks()
            })
            .catch(error => {
                console.log(error)
			})

		//setBooks(books.filter(book => book.id !== _id))
	}

	const updateBook = (_id, book) => {
		// setEditing(false)
		// setBooks(books.map(book => (book.id === id ? updatedBook : book)))

		console.log("_id: " + _id)
		console.log("updateBook id: " + book._id)

		axios.put("http://localhost:5000/books/" + _id, book)
            .then(response => {
				console.log(response)
				getBooks()
            })
            .catch(error => {
                console.log(error)
			})
	}

	const editRow = book => {
		console.log("editRow: " + book._id)
		setEditing(true)
		console.log(book)
		setCurrentBook({ _id: book._id, title: book.title, author: book.author, price: book.price })		
	}

	return (
		<div className="container">
			<h1>华夏中文学校-图书列表管理</h1>
			<div>
				<Popup addBook={addBook}/>
			</div>
			<div className="flex-row">
				{/* <div className="flex-large">
					{editing ? (
						<Fragment>
							<h2>Edit book</h2>
							<EditBookForm
								editing={editing}
								setEditing={setEditing}
								currentBook={currentBook}
								updateBook={updateBook}
							/>
						</Fragment>
					) : (
						<Fragment>
							<h2>Add book</h2>
							<AddBookForm addBook={addBook} />
						</Fragment>
					)}
				</div> */}
				<div className="flex-large">
					<h2>View books</h2>
					<BookTable books={books} editRow={editRow} deleteBook={deleteBook} />
				</div>
			</div>
		</div>
	)
}

export default BookManager
