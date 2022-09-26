import React, { FC, MouseEvent } from "react";
import { IExample } from "./Examples";
import styles from "./CodeSnippet.module.scss";
import { ReactComponent as PlayIcon } from "../../assets/SVG/play3.svg";

const CodeSnippet: FC<{
  code: IExample;
  onRunSnippet: (
    event: MouseEvent<HTMLButtonElement>,
    snippetCode: string
  ) => void;
}> = ({ code, onRunSnippet }) => {
  return (
    <div className={styles.snippet}>
      <h2>{code.title}</h2>
      <h4>{code.description}</h4>
      <div className={styles.code}>
        {code.code.split("\n").map((line, index) => (
          <p key={index}>{line}</p>
        ))}
      </div>
      <div className={styles.control}>
        <button
          className={styles.button}
          onClick={(e) => onRunSnippet(e, code.code)} 
        >
          <PlayIcon /> Run
        </button>
      </div>
    </div>
  );
};

export default CodeSnippet;
