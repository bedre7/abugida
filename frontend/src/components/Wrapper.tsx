import React, { ReactNode } from "react";
import styles from "./Wrapper.module.scss";

const Wrapper: React.FC<{ children: ReactNode }> = (props) => {
  return <div className={styles.wrapper}>{props.children}</div>;
};

export default Wrapper;
