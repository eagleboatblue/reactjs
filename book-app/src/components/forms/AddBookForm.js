import React, { useState } from 'react'
import styles from "./wang.css"

const AddBookForm = props => {
	const initialFormState = { _id: null, title: '', author: '', price: '',read:false, rating:0 }
	const [ book, setBook ] = useState(initialFormState)

	const handleInputChange = event => {
		const { name, value } = event.target

		setBook({ ...book, [name]: value })
	}

	return (
		<form
			onSubmit={event => {
				event.preventDefault()
				if (!book.title || !book.author) return

				props.addBook(book)
				setBook(initialFormState)
			}}
		>
			<label>Title</label>
			<input type="text" name="title" value={book.title} onChange={handleInputChange} />
			<label>Author</label>
			<input type="text" name="author" value={book.author} onChange={handleInputChange} />
			<label>Price</label>
			<input type="text" name="price" value={book.price} onChange={handleInputChange} />
			<button className={styles.danger}>Add new book</button>
		</form>
	)
}

export default AddBookForm
