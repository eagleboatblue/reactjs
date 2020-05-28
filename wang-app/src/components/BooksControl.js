import React, { Component } from 'react'
import BookChange from './BookChange'

export default class BooksControl extends Component {
    state = {
        bookArray : [
          {
            id : 1,
            title : "How to cook",
            author : "Weiping Xing",
            price : 99.99
          },
          {
            id : 2,
            title : "Running Skills",
            author : "John Wang",
            price : 45.00
          },
          {
            id : 3,
            title : "Sleep and eat well",
            author : "Jun Wu",
            price : 99.99
          }
        ]
      }
    
      deleteEvent = (index) => {
        const copyBookArray = Object.assign([], this.state.bookArray);
        copyBookArray.splice(index, 1);
        this.setState({
            bookArray : copyBookArray
        })
      }

    render() {
        return (
            <div>
                <font color="darkblue" size="3">华夏中文学校-图书列表</font>
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
