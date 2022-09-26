import React, { useState, FC } from "react";
import { CodeContext } from "./CodeContext";
import { RunCodeRequest } from "../api/RunCodeRequest";
import useLocalStorage from "../hooks/useLocalStorage";

const CodeContextProvider: FC<{ children: React.ReactNode }> = (props) => {
  const [terminalIsVisible, setTerminalIsVisible] = useState(true);
  const [isRunning, setIsRunning] = useState(false);
  const [output, setOutput] = useState<string[]>([]);
  const [error, setError] = useState<string[]>([]);
  const [code, setCode] = useLocalStorage("code", 'PRINT: "Hello World!"');
  const [lines, setLines] = useState<number[]>([1]);

  const runCodeHandler = async (code: string) => {
    setTerminalIsVisible(true);
    try {
      setIsRunning(true);
      const { output, error } = await RunCodeRequest(code);

      setOutput(output);
      setError(error);
    } catch (error: any) {
      setError([error.message]);
    } finally {
      setIsRunning(false);
    }
  };

  return (
    <CodeContext.Provider
      value={{
        code,
        lines,
        output,
        error,
        isRunning,
        terminalIsVisible,
        setCode,
        setLines,
        setTerminalIsVisible,
        runCodeHandler,
      }}
    >
      {props.children}
    </CodeContext.Provider>
  );
};

export default CodeContextProvider;
