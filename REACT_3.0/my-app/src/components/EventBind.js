import React, { Component } from 'react'

class EventBind extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
             message: 'Hello'
        }

        this.xyz = this.abe.bind(this)
    }
    
    abe() {
        this.setState(
            {
                message: 'Good Bye'
            }
        )
        console.log(this)
    }
    render() {
        return (
            <div>
                <div>{this.state.message}</div>
                {/* <button onClick = {this.clickHandler.bind(this)}>Click</button>  */}
                {/* <button onClick = {() => this.clickHandler()}>Click</button> */}
                <button onClick = {this.xyz}>Click</button>
            </div>
        )
    }
}

export default EventBind
