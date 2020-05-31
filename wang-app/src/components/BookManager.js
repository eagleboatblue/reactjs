import React, { useState, Fragment } from 'react'
import AddBookForm from './forms/AddBookForm'
import EditBookForm from './forms/EditBookForm'
import BookTable from './tables/BookTable'

const BookManager = () => {
	// Data
	const booksData = [
		{ id: 1, title: 'How to running', author: 'floppydiskette', price: '99.30' },
		{ id: 2, title: 'War II', author: 'siliconeidolon', price: '52.99'  },
		{ id: 3, title: 'Cooking skillset', author: 'benisphere', price: '9.60'  },
	]

	const initialFormState = { id: null, title: '', author: '', price: '' }

	// Setting state
	const [ books, setBooks ] = useState(booksData)
	const [ currentBook, setCurrentBook ] = useState(initialFormState)
	const [ editing, setEditing ] = useState(false)

	// CRUD operations
	const addBook = book => {
		book.id = books.length + 1
		setBooks([ ...books, book ])
	}

	const deleteBook = id => {
		setEditing(false)

		setBooks(books.filter(book => book.id !== id))
	}

	const updateBook = (id, updatedBook) => {
		setEditing(false)

		setBooks(books.map(book => (book.id === id ? updatedBook : book)))
	}

	const editRow = book => {
		setEditing(true)

		setCurrentBook({ id: book.id, title: book.title, author: book.author, price: book.price })
	}

	return (
		<div className="container">
			<h1>华夏中文学校-图书列表管理</h1>
			<div className="flex-row">
				<div className="flex-large">
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
				</div>
				<div className="flex-large">
					<h2>View books</h2>
					<BookTable books={books} editRow={editRow} deleteBook={deleteBook} />
				</div>
			</div>
		</div>
	)
}

export default BookManager
