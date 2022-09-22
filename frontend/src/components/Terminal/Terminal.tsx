import React, { FC } from "react";
import Layout from "../UI/Layout";
import Spinner from "../UI/Spinner";
import styles from "./Terminal.module.scss";

const Terminal: FC<{
  onClose: (event: React.MouseEvent<HTMLElement>) => void;
  isRunning: boolean;
}> = ({ onClose, isRunning }) => {
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
        </div>
      </div>
    </Layout>
  );
};

export default Terminal;
