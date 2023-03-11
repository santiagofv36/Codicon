import React, { useState } from "react";
import "./Navbar.css";
import { RiMenu3Line, RiCloseLine } from "react-icons/ri";
import Logo from "../../assets/Logo.png";
import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";



function Navbar({ handleLoginClick }) {
  const [toggle, setToggle] = useState(false);
  const navigate = useNavigate();


    const handleLogin = () => {
        handleLoginClick();
    }

    const navigateToCaja = () => {
        navigate("/Cajas");
    }

    const navigateToHome = () => {
        navigate("/");
    }

    const navigateToSubastas = () => {
        navigate("/Subastas");
    }

    const navigateToInventario = () => {
        navigate("/Inventario");
    }

    const navigateToMejoras = () => {
        navigate("/Mejoras");
    }

    const Menu = () => {


      return (
        <>
          <p onClick={navigateToSubastas}>Subastas</p>
          <p onClick={navigateToCaja}>Cajas</p>
          <p onClick={navigateToInventario}>Inventario</p>
          <p onClick={navigateToMejoras}>Mejoras</p>
        </>
      );
    };

  return (
    <div className="navbar bg_gradient">
      <div className="navbar-links">
        <div className="navbar-links_logo">
            <img src={Logo} onClick={navigateToHome}/>
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
                <p onClick={handleLogin}>Iniciar Sesión</p>
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
