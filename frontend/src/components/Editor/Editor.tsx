import React, { ChangeEvent, useState, useRef, FC } from "react";
import Layout from "../UI/Layout";
import styles from "./Editor.module.scss";

const Editor: FC<{ isFullSize: boolean; onRun: (code: string) => void }> = ({
  isFullSize,
  onRun,
}) => {
  const [lines, setLines] = useState([1]);
  const [code, setCode] = useState("");
  const lineBarRef = useRef<HTMLDivElement>(null);

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
      filename="Abugida.abg"
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
