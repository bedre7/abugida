import React, { FC, useContext } from "react";
import Layout from "../UI/Layout";
import Spinner from "../UI/Spinner";
import styles from "./Terminal.module.scss";
import { CodeContext, ICode } from "../../context/CodeContext";

interface TerminalProps {
  onClose: (event: React.MouseEvent<HTMLElement>) => void;
}

const Terminal: FC<TerminalProps> = ({ onClose }) => {
  const { isRunning, output, error } = useContext(CodeContext) as ICode;
  
  return (
    <Layout
      filename="command line"
      element="terminal"
      buttonType="close"
      clickHandler={onClose}
    >
      <div className={styles.terminal}>
        <div className={styles.output}>
          {isRunning && <Spinner />}
          <p style={{ color: "lightgreen" }}>$ output</p>
          <p style={{ color: "cyan" }}>@Abugida/App.abg &gt;&gt;</p>
          {output && output.map((line, index) => <p key={index}>{line}</p>)}
          {error &&
            error.map((line) =>
              line.split("\n").map((line, index) => (
                <p key={index} style={{ color: "orangered" }}>
                  {line}
                </p>
              ))
            )}
        </div>
      </div>
    </Layout>
  );
};

export default Terminal;
