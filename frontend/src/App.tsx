import React, { useState } from "react";
import { Routes, Route } from "react-router-dom";
import Home from "./components/Home/Home";
import About from "./components/About/About";
import SideBar from "./components/SideBar/SideBar";
import Examples from "./components/Examples/Examples";
import MenuBar from "./components/SideBar/MenuBar";
import Documentation from "./components/Documentation/Documentation";
import "./App.scss";

const App = () => {
  const [showSideBar, setShowSideBar] = useState(true);

  const clickHandler = () => {
    setShowSideBar((prevState) => !prevState);
  };

  return (
    <div className="App">
      {showSideBar && <SideBar />}
      <MenuBar onClose={clickHandler} />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/About" element={<About />} />
        <Route path="/Documentation" element={<Documentation />} />
        <Route path="/Examples" element={<Examples />} />
      </Routes>
    </div>
  );
};

export default App;
