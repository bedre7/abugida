import React, { FC, MouseEvent } from "react";
import { IExample } from "./Examples";
import styles from "./CodeSnippet.module.scss";
import { ReactComponent as PlayIcon } from "../../assets/SVG/play3.svg";

const CodeSnippet: FC<{
  code: IExample;
  onRunSnippet: (
    event: MouseEvent<HTMLButtonElement>,
    snippetCode: string[]
  ) => void;
}> = ({ code, onRunSnippet }) => {
  return (
    <div className={styles.snippet}>
      <h2>{code.title}</h2>
      <h4>{code.description}</h4>
      <ul className={styles.code}>
        {code.codes.map((snippet, index) => (
          <li key={index}>
            {snippet.split("\n").map((line, index) => (
              <p key={index}>{line}</p>
            ))}
          </li>
        ))}
      </ul>
      <div className={styles.control}>
        <button
          className={styles.button}
          onClick={(e) => onRunSnippet(e, code.codes)}
        >
          <PlayIcon /> Run
        </button>
      </div>
      <div className={styles.control}></div>
    </div>
  );
};

export default CodeSnippet;
