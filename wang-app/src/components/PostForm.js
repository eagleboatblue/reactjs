import React, { Component } from 'react'
import axios from 'axios'

class PostForm extends Component {

    constructor(props) {
        super(props)

        this.state = {
            title: '',
            author: '',
            price: 0,
            rating:0,
            read:false
        }
    }

    changeHandler = (e) => {
        this.setState({[e.target.name]:e.target.value})
    }

    submitHandler = (e) => {
        e.preventDefault()
        console.log(this.state)
        axios.post("http://localhost:5000/books",this.state)
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
            <div>
                <form onSubmit={this.submitHandler}>
                    <div>
                        <input type="text" name="title" value={title} onChange={this.changeHandler} />
                    </div>
                    <div>
                        <input type="text" name="author" value={author} onChange={this.changeHandler} />
                    </div>
                    <div>
                        <input type="text" name="price" value={price} onChange={this.changeHandler} />
                    </div>
                    <button type="submit">Submit</button>
                </form>
            </div>
        )
    }
}

export default PostForm