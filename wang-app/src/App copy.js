import React, { useEffect, useState } from 'react';
import './App.css';
import * as ReactBootStrape from 'react-bootstrap';
import BookComp from './components/BookComp'
import BookChange from './components/BookChange'
import { Component } from 'react';

export default class App extends Component {
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

  render(){
    return (
      <div>
        <ul>
          {
            this.state.bookArray.map((post, index) => {
              this.return(
                <BookComp
                  id = {post.id}
                  title = {post.title}
                  author = {post.author}
                  price = {post.price}
                />
              )
            })
          }
        </ul>
      </div>
    )
  } 
}
