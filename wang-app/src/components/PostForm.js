import React, { Component} from 'react'
import axios from 'axios'
import BookComp from './BookComp'

class PostForm extends Component {

    constructor(props) {
        super(props)

        this.state = {
            title: '',
            author: '',
            price: 0,
            rating: 0,
            read: false
        }
    }

    changeHandler = (e) => {
        this.setState({ [e.target.name]: e.target.value })
    }

    submitHandler = (e) => {
        e.preventDefault()
        console.log(this.state)
        axios.post("http://localhost:5000/books", this.state)
            .then(response => {
                console.log(response)
            })
            .catch(error => {
                console.log(error)
            })
    }


    render() {
        const { title, author, price } = this.state
        return (
            <div  className="flex-row">
                <form onSubmit={this.submitHandler}>
                    <div>
                        <label>Add new book</label>
                        <table>
                            <tr><td align="right"><label>Title: </label></td>
                                <td><input type="text" name="title" value={title} onChange={this.changeHandler} /></td>
                            </tr>
                            <tr>
                                <td><label>Author:</label></td>
                                <td><input type="text" name="author" value={author} onChange={this.changeHandler} /></td>
                            </tr>
                            <tr>
                                <td><label>Price:</label></td>
                                <td><input type="text" name="price" value={price} onChange={this.changeHandler} /></td>
                            </tr>
                        </table>
                    </div>
                    <button type="submit">Add New Book</button>
                </form>
                <BookComp />
            </div>
        )
    }
}

export default PostForm