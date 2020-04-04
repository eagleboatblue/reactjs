import React from 'react'

//function Greet() {
//    return <h1>Hello my friends, Good morning</h1>
//}

const Greet = props => {
    
    const {name, heroname} = props
    console.log(name, heroname)
    return (
        <div>
            <h1>Hello I am here {name} a.k.a {heroname}</h1>
            { props.children}
        </div>
    )
}
export default Greet