import React, { FC } from "react";
import Layout from "../UI/Layout";
import Spinner from "../UI/Spinner";
import styles from "./Terminal.module.scss";

interface TerminalProps {
  onClose: (event: React.MouseEvent<HTMLElement>) => void;
  isRunning: boolean;
  output: string[];
  error: string[];
}

const Terminal: FC<TerminalProps> = ({ onClose, isRunning, output, error }) => {
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
          <p>$ output</p>
          {output && output.map((line, index) => <p key={index}>{line}</p>)}
          {error &&
            error.map((line, index) => (
              <p style={{ color: "orangered" }} key={index}>
                {line}
              </p>
            ))}
        </div>
      </div>
    </Layout>
  );
};

export default Terminal;
