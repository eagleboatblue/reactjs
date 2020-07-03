import React from 'react'

const BookTable = props => (
  <table>
    <thead>
      <tr bgcolor="lightblue">
        <th>Title</th>
        <th>Author</th>
        <th>Price</th>
        <th>Actions</th>
      </tr>
    </thead>
    <tbody>
      {props.books.length > 0 ? (
        props.books.map(book => (
          <tr key={book._id} >
            <td>{book.title}</td>
            <td>{book.author}</td>
            <td>{book.price}</td>
            <td>
              <button
                onClick={() => {
                  props.editRow(book)
                }}
                class="btn btn-warning"
               >
                Edit
              </button>
              <button
                onClick={() => props.deleteBook(book._id)}
                class="btn btn-danger"
              >
                Delete
              </button>
            </td>
          </tr>
        ))
      ) : (
        <tr>
          <td colSpan={3}>Sorry, No any book.</td>
        </tr>
      )}
    </tbody>
  </table>
)

export default BookTable
