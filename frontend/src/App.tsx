import React from "react";
import "./App.css";
import Editor from "./components/Editor/Editor";
import SideBar from "./components/SideBar/SideBar";
import Terminal from "./components/Terminal/Terminal";
import Wrapper from "./components/Wrapper";

const App = () => {
  return (
    <div className="App">
      <SideBar />
      <Wrapper>
        <Editor />
        <Terminal />
      </Wrapper>
    </div>
  );
};

export default App;
