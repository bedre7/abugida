import React, { useState } from "react";
import { RunCodeRequest } from "./api/RunCodeRequest";
import Editor from "./components/Editor/Editor";
import SideBar from "./components/SideBar/SideBar";
import Terminal from "./components/Terminal/Terminal";
import Wrapper from "./components/UI/Wrapper";
import "./App.css";

const App = () => {
  const [terminalIsVisible, setTerminalIsVisible] = useState(true);
  const [isRunning, setIsRunning] = useState(false);
  const [output, setOutput] = useState([]);
  const [error, setError] = useState([]);

  const closeTerminal = () => {
    setTerminalIsVisible(false);
  };

  const runCodeHandler = async (code: string) => {
    setTerminalIsVisible(true);
    try {
      setIsRunning(true);
      const { output, error } = await RunCodeRequest(code);

      setOutput(output);
      setError(error);

    } catch (error: any) {
      setError(error);
    } finally {
      setIsRunning(false);
    }
  };

  return (
    <div className="App">
      <SideBar />
      <Wrapper>
        <Editor isFullSize={!terminalIsVisible} onRun={runCodeHandler} />
        {terminalIsVisible && (
          <Terminal
            onClose={closeTerminal}
            isRunning={isRunning}
            output={output}
            error={error}
          />
        )}
      </Wrapper>
    </div>
  );
};

export default App;
