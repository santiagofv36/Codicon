import React, { useState } from 'react';
import './Login.css';

const Login = ({isShowingLogin, onClose}) => {

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleLogin = (e) => {
        e.preventDefault();
        console.log(email, password);
        /* */
    }

  return (
    <div className={`${isShowingLogin ? "active": ""} show`}>
        {
            !isShowingLogin &&(

        <div className="login">
            <div className='login-close-btn'>
                <button type="button" onClick={onClose}>X</button>
            </div>
            <div className='login-form'>
                <form onSubmit={handleLogin}>
                    <div className='login-form-header'>
                        <h3>Iniciar Sesión</h3>
                    </div>
                    <div className="login-form__group">
                        <label name="email">Email</label>
                        <input type="email" name="email" id="email" placeholder="Email" onChange={(e)=> setEmail(e.target.value)}/>
                    </div>
                    <div className="login-form__group">
                        <label name="password">Password</label>
                        <input type="password" name="password" id="password" placeholder="Password" onChange={(e)=> setPassword(e.target.value)}/>
                    </div>
                    <div className="login-form__group">
                        <button type="submit">Iniciar Sesión</button>
                    </div>
                </form>
            </div>    
        </div>
            )
        }
    </div>
  );
};



export default Login;

