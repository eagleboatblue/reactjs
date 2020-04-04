import React, { Component } from 'react'

class LifecycleB extends Component {
    constructor(props) {
        super(props)
    
        this.state = {
             name: 'Vishwas'
        }

        console.log('LifecycleB consturctor')
    }
    
    static getDerviedStateFromProps(props, state){
        console.log('LifecycleB getDerviedStateFromProps')
        return null
    }

    componentDidMount() {
        console.log('LifecycleB componentDidMount')
    }

    shouldComponentUpdate()
    {
        console.log('LifecycleB shouldComponentUpdate')
    }

    getSnapshotBeforeUpdate(preProps, preState){
        console.log('LifecycleB getSnapshotBeforeUpdate')
        return null
    }

    componentDidUpdate() {
        console.log('LifecycleB componentDidUpdate')
    }

    render() {
        console.log('LifecycleB render')
        return (
            <div> 
                Lifecycle B            
            </div>
        )
    }
}

export default LifecycleB
