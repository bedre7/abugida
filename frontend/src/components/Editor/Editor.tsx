import React, { ChangeEvent, useState } from "react";
import Layout from "../Layout";
import styles from "./Editor.module.scss";

const Editor = () => {
  const [lines, setLines] = useState([1]);
  const [code, setCode] = useState("");

  const textChangeHandler = (event: ChangeEvent<HTMLTextAreaElement>) => {
    const { value } = event.target;
    if (value == "") setLines([1]);
    else {
      const numberOfLines = value.split(/\r*\n/).length;

      for (let i = 1; i <= numberOfLines; i++) {
        setLines((prevLines) => Array.from(new Set([...prevLines, i])));
      }
    }
    setCode(value);
  };

  return (
    <Layout filename="Abugida.abg" buttonType="run">
      <div className={styles.input}>
        <div className={styles.linebar}>
          {lines.map((line) => {
            return <span key={line}>{line}</span>;
          })}
        </div>
        <textarea
          name="code"
          id="code"
          draggable={false}
          spellCheck={false}
          onChange={textChangeHandler}
        />
      </div>
    </Layout>
  );
};

export default Editor;
