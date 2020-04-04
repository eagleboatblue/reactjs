import React, { Component } from 'react'

class UserGreeting extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
             isLoggingIn: true
        }
    }
    
    render() {

        return this.state.isLoggingIn && <div>Welcome Host</div>

        // return (
        //     this.state.isLoggingIn ?
        //     <div>Welcome Host</div> :
        //     <div>Welcome Guess</div>
        // )

        // let message
        // if (this.state.isLoggingIn)
        // {
        //     message = <div>Welcome Host</div>
        // }
        // else{
        //     message = <div>Welcome Guest</div>
        // }

        // return <div>{message}</div>

        // if (this.state.isLoggingIn) {
        //     return (
        //         <div>
        //             <div>Welcome Host</div>
        //         </div>
        //     )
        // }
        // else {
        //     return (
        //         <div>
        //             <div>Welcome Guest</div>
        //         </div>
        //     )
        // }
    }
}

export default UserGreeting
