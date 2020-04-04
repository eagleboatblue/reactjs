import React from 'react'

function FunctionClick() {
    
    function clickHandler() {
        console.log('Button clicked in FUNCTION')
    }
    return (
        <div>
            <button onClick={clickHandler}>Click</button>
        </div>
    )
}

export default FunctionClick
