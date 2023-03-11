import "./App.css";
import React, { useState } from "react";
import { Navbar, Home, Login, Footer, Box } from "./Components";
import { Routes, Route } from "react-router-dom";

function App() {

  const [isShowingLogin, setIsShowingLogin] = useState(true);

  const handleLoginClick = ()=> {
    setIsShowingLogin(!isShowingLogin);
  }

  return (
    <div className="App">
      <Navbar handleLoginClick={handleLoginClick}/>
      <Login isShowingLogin={isShowingLogin} onClose={handleLoginClick}/>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/Cajas" element={<Box />} />
      </Routes>
      <Footer/>
    </div>
  );
}

export default App;
