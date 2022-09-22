import React from "react";
import styles from "./Spinner.module.scss";

const Spinner = () => {
  return <div className={styles.spinner}>
    <div className={styles.circle}></div>
    <p>Running...</p>
  </div>;
};

export default Spinner;
