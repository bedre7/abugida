import React, { useState, FC, Dispatch, SetStateAction } from "react";
import Wrapper from "../UI/Wrapper";
import Editor from "../Editor/Editor";
import styles from "./Home.module.scss";
import Terminal from "../Terminal/Terminal";
import { RunCodeRequest } from "../../api/RunCodeRequest";

const Home: FC<{ setShowSideBar: Dispatch<SetStateAction<boolean>> }> = ({
  setShowSideBar,
}) => {
  const [terminalIsVisible, setTerminalIsVisible] = useState(true);
  const [isRunning, setIsRunning] = useState(false);
  const [output, setOutput] = useState<string[]>([]);
  const [error, setError] = useState<string[]>([]);

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
      console.log(error);
    } catch (error: any) {
      setError([error.message]);
    } finally {
      setIsRunning(false);
    }
  };

  return (
    <div className={styles.home}>
      <Wrapper>
        <Editor
          isFullSize={!terminalIsVisible}
          onRun={runCodeHandler}
          showSideBar={() => setShowSideBar((prevState) => !prevState)}
        />
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

export default Home;
