import React, { useState } from "react";
import { Routes, Route } from "react-router-dom";
import Home from "./components/Home/Home";
import About from "./components/About/About";
import SideBar from "./components/SideBar/SideBar";
import Examples from "./components/Examples/Examples";
import Documentation from "./components/Documentation/Documentation";
import { ReactComponent as MenuIcon } from "./assets/SVG/menu.svg";
import "./App.scss";

const App = () => {
  const [showSideBar, setShowSideBar] = useState(true);

  return (
    <div className="App">
      {showSideBar && <SideBar />}
      <button className="menu" onClick={() => setShowSideBar((prevState) => !prevState)}>
        <MenuIcon />
      </button>
      <Routes>
        <Route path="/" element={<Home setShowSideBar={setShowSideBar} />} />
        <Route path="/About" element={<About />} />
        <Route path="/Documentation" element={<Documentation />} />
        <Route path="/Examples" element={<Examples />} />
      </Routes>
    </div>
  );
};

export default App;
