import React, { Component } from 'react'

class BookChange extends Component {

    render() {
        return (
            <div>
                <li>
                    id : {this.props.id}
                    <br/>
                    title : {this.props.title}
                    <br/>
                    author : {this.props.author}
                    <br/>
                    price : {this.props.price}
                    <br/>
                    <button onClick={this.props.delete}>Update</button>
                    <button onClick={this.props.delete}>Delete</button>
                    <hr/>
                </li>
            </div>
        )
    }
}

export default BookChange