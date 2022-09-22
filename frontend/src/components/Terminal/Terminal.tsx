import React from "react";
import Layout from "../Layout";
import styles from "./Terminal.module.scss";

const Terminal = () => {
  return (
    <Layout filename="command line" element="terminal" buttonType="close">
      <div className={styles.terminal}>
        <div className={styles.output}>
          <p>$ output</p>
        </div>
      </div>
    </Layout>
  );
};

export default Terminal;
