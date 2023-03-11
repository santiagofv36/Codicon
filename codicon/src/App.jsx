import "./App.css";
import React, { useState } from "react";
import { Navbar, Home, Login, Footer } from "./Components";

function App() {

  const [isShowingLogin, setIsShowingLogin] = useState(true);

  const handleLoginClick = ()=> {
    setIsShowingLogin(!isShowingLogin);
  }

  return (
    <div className="App">
      <Navbar handleLoginClick={handleLoginClick}/>
      <Login isShowingLogin={isShowingLogin} onClose={handleLoginClick}/>
      <Home />
      <Footer/>
    </div>
  );
}

export default App;
