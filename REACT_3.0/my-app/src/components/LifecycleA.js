import React, { Component } from 'react'
import LifecycleB from './LifecycleB'

class LifecycleA extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
             name: ''
        }

        console.log('LifecycleA consturctor')
    }
    
    static getDerviedStateFromProps(props, state){
        console.log('LifecycleA getDerviedStateFromProps')
        return null
    }

    componentDidMount(){
        console.log('LifecycleA componentDidMount')
    }

    shouldComponentUpdate()
    {
        console.log('LifecycleA shouldComponentUpdate')
        return null
    }

    getSnapshotBeforeUpdate(preProps, preState){
        console.log('LifecycleA getSnapshotBeforeUpdate')
        return null
    }

    componentDidUpdate() {
        console.log('LifecycleA componentDidUpdate')
    }

    changeState = () => {
        this.setState({
            name: 'Codevolution'
        })
    }

    render() {
        console.log('LiftcycleA render')
        return (
            <div> 
                <div>Lifecycle A</div>
                <button onClick={this.changeState}>Change state</button>
                <LifecycleB />          
            </div>
        )
    }
}

export default LifecycleA
