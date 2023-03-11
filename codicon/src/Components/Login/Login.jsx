import React, { useState } from 'react';
import './Login.css';

const Login = ({isShowingLogin, onClose}) => {

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const validateFields = () => {
        if(email.length === 0 || password.length === 0){
            return false;
        }
        return true;
    }

    const handleLogin = (e) => {
        e.preventDefault();
        console.log(email, password);
        /* */
    }

  return (
    <div>

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
                        <input maxLength='35' type="email" name="email" id="email" placeholder="Email" onChange={(e)=> setEmail(e.target.value)}/>
                    </div>
                    <div className="login-form__group">
                        <label name="password">Password</label>
                        <input minLength='8' maxLength='25'type="password" name="password" id="password" placeholder="Password" onChange={(e)=> setPassword(e.target.value)}/>
                    </div>
                    {
                        !validateFields() && (
                            <div className='login-form__error'>
                                <p>¡Usuario o contraseña incorrectos!</p>
                            </div>
                        )
                    }
                    <div className='login-form__signup'>
                        <p>¿No tienes una cuenta? Registrate</p>
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
        {!isShowingLogin && <div className='overlay'></div>}
    </div>
  );
};



export default Login;

