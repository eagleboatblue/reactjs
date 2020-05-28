import React, { Component } from 'react'
import BookChange from './BookChange'

export default class BooksControl extends Component {
    constructor() {
        super();
        this.bookId = 0;
        this.title = "";
        this.author = "";
        this.price = 0;

        this.state = {
            bookArray : []
        }
    }
      deleteEvent = (index) => {
        const copyBookArray = Object.assign([], this.state.bookArray);
        copyBookArray.splice(index, 1);
        this.setState({
            bookArray : copyBookArray
        })
      }

      setTitle = (element) => {
          this.title =  element.target.value
      }

      setAuthor = (element) => {
        this.author =  element.target.value
      }

      setPrice = (element) => {
        this.price =  element.target.value
      }

      setBook = (element) => {
        this.setState({
            title : element.target.value,
            author : element.target.value,
            price : element.target.value
        })
      }

      addBook = () => {
        this.bookId = this.bookId + 1;
        const copyBookArray = Object.assign([], this.state.bookArray);
        copyBookArray.push({
            id : this.bookId,
            title : this.title,
            author : this.author,
            price : this.price
        })
        this.setState({
            bookArray : copyBookArray
        })
      }

    render() {
        return (
            <div>
                <font color="darkblue" size="3">华夏中文学校-图书列表</font>
                <br></br>
                <button onClick={this.addBook}>Add</button>
                <input type="text" name="Title" onBlur = {this.setTitle} />
                <input type="text" name="Author" onBlur = {this.setAuthor} />
                <input type="text" name="Price" onBlur = {this.setPrice} />
                <ul>
                {
                    this.state.bookArray.map((post, index) => {
                        return(
                            <BookChange
                                key = {post.id}
                                id = {post.id}
                                title = {post.title}
                                author = {post.author}
                                price = {post.price}
                                delete = {this.deleteEvent.bind(this, index)}
                            />
                            )
                    })
                }
                </ul>
            </div>
        ) 
    }
}
