import React from 'react'
import './MyStyles.css'

function Stylesheet(props) {
    
    //let colorType = props.primary ? 'primary' : ''

    let colorType = 'primary'

    return (
        <div>
            <h1 className={colorType}>Stylesheets</h1>
        </div>
    )
}

export default Stylesheet
