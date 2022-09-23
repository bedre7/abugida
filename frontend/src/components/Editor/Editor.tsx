import React, { ChangeEvent, useState, useRef, FC } from "react";
import useLocalStorage from "../../hooks/useLocalStorage";
import Layout from "../UI/Layout";
import styles from "./Editor.module.scss";

interface EditorProps {
  isFullSize: boolean;
  onRun: (code: string) => void;
}

const Editor: FC<EditorProps> = ({ isFullSize, onRun }) => {
  const [code, setCode] = useLocalStorage("code", 'PRINT: "Hello World!"');
  const lineBarRef = useRef<HTMLDivElement>(null);
  const [lines, setLines] = useState([1]);

  const textChangeHandler = (event: ChangeEvent<HTMLTextAreaElement>) => {
    const { value } = event.target;
    if (value === "") setLines([1]);
    else {
      const numberOfLines = value.split(/\r*\n/).length;

      for (let i = 1; i <= numberOfLines; i++) {
        setLines((prevLines) => Array.from(new Set([...prevLines, i])));
      }
    }
    setCode(value);
  };

  const scrollHandler = (
    event: React.UIEvent<HTMLTextAreaElement, UIEvent>
  ) => {
    lineBarRef!.current!.scrollTop = event.currentTarget.scrollTop;
  };

  const runCode = () => {
    onRun(code);
  };

  return (
    <Layout
      filename="App.abg"
      buttonType="run"
      text="Run"
      clickHandler={runCode}
    >
      <div className={styles.input}>
        <div
          className={styles.linebar}
          ref={lineBarRef}
          style={{ height: `${isFullSize ? "100vh" : "58vh"}` }}
        >
          {lines.map((line) => {
            return <span key={line}>{line}</span>;
          })}
        </div>
        <textarea
          value={code}
          name="code"
          id="code"
          draggable={false}
          spellCheck={false}
          onChange={textChangeHandler}
          onScroll={scrollHandler}
        />
      </div>
    </Layout>
  );
};

export default Editor;
