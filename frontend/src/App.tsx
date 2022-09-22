import React, { useState } from "react";
import "./App.css";
import Editor from "./components/Editor/Editor";
import SideBar from "./components/SideBar/SideBar";
import Terminal from "./components/Terminal/Terminal";
import Wrapper from "./components/UI/Wrapper";

const App = () => {
  const [terminalIsVisible, setTerminalIsVisible] = useState(true);
  const [isRunning, setIsRunning] = useState(true);

  const closeTerminal = () => {
    setTerminalIsVisible(false);
  };

  const runCodeHandler = (code: string) => {
    setTerminalIsVisible(true);
  }

  return (
    <div className="App">
      <SideBar />
      <Wrapper>
        <Editor isFullSize={!terminalIsVisible} onRun={runCodeHandler}/>
        { terminalIsVisible && <Terminal onClose={closeTerminal} isRunning={isRunning}/> }
      </Wrapper>
    </div>
  );
};

export default App;
