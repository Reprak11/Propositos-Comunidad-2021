import React from 'react'
import logo from '../assets/dlogo.png'


const LogoBox = () => {
    return(
        <div className="logo-box">
            <img className="logo-style" src={logo} alt="#" />
            <button className="add-goal">Agrega tu propósito</button>
        </div>
)
}

export default LogoBox