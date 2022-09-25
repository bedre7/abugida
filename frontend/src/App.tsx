import React, { useState } from "react";
import { Routes, Route } from "react-router-dom";
import Home from "./components/Home/Home";
import Examples from "./components/Examples/Examples";
import Documentation from "./components/Documentation/Documentation";
import SideBar from "./components/SideBar/SideBar";
import "./App.scss";

const App = () => {
  const [showSideBar, setShowSideBar] = useState(true);

  return (
    <div className="App">
      {showSideBar && <SideBar />}
      <Routes>
        <Route path="/" element={<Home setShowSideBar={setShowSideBar} />} />
        <Route path="/Documentation" element={<Documentation />} />
        <Route path="/Examples" element={<Examples />} />
      </Routes>
    </div>
  );
};

export default App;
