import React, { useState } from "react";
import "./Navbar.css";
import { RiMenu3Line, RiCloseLine } from "react-icons/ri";
import Logo from "../../assets/Logo.png";


const Menu = () => {
  return (
    <>
      <p>Subastas</p>
      <p>Cajas</p>
      <p>Inventario</p>
      <p>Mejoras</p>
    </>
  );
};


function Navbar({ handleLoginClick }) {
  const [toggle, setToggle] = useState(false);


    const handleLogin = () => {
        handleLoginClick();
    }

  return (
    <div className="navbar bg_gradient">
      <div className="navbar-links">
        <div className="navbar-links_logo">
          <img src={Logo} />
        </div>
        <div className="navbar-links_container">
          <Menu />
        </div>
      </div>
      <div className="navbar-sign">
        <p onClick={handleLogin}>Iniciar Sesión</p>
        <button type="button">Registrarse</button>
      </div>
      <div className="navbar-menu">
        {toggle ? (
          <RiCloseLine
            color="#fff"
            size={35}
            onClick={() => setToggle(!toggle)}
          />
        ) : (
          <RiMenu3Line
            color="#fff"
            size={35}
            onClick={() => setToggle(!toggle)}
          />
        )}
        {toggle && (
          <div className="navbar-menu_container scale-up-center">
            <div className="navbar-menu_container-links">
              <Menu />
              <div className="navbar-menu_container-links-sign">
                <p>Iniciar Sesión</p>
                <button type="button">Registrarse</button>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default Navbar;
