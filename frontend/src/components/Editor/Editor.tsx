import React, { ChangeEvent, useContext, useRef, useEffect, FC } from "react";
import Layout from "../UI/Layout";
import styles from "./Editor.module.scss";
import { ReactComponent as MenuIcon } from "../../assets/SVG/menu.svg";
import { CodeContext, IContext } from "../../context/CodeContext";

interface EditorProps {
  isFullSize: boolean;
  showSideBar: () => void;
}

const Editor: FC<EditorProps> = ({ isFullSize, showSideBar }) => {
  const lineBarRef = useRef<HTMLDivElement>(null);
  const {code, lines, setCode, setLines, runCodeHandler} = useContext(CodeContext) as IContext;

  const updateLines = (value: string) => {
    if (value === "") setLines([1]);
    else {
      const numberOfLines = value.split(/\r*\n/).length;
      setLines([]);
      for (let i = 1; i <= numberOfLines; i++) {
        setLines((prevLines) => Array.from(new Set([...prevLines, i])));
      }
    }
  };

  const textChangeHandler = (event: ChangeEvent<HTMLTextAreaElement>) => {
    const { value } = event.target;
    updateLines(value);
    setCode(value);
  };

  const scrollHandler = (
    event: React.UIEvent<HTMLTextAreaElement, UIEvent>
  ) => {
    lineBarRef!.current!.scrollTop = event.currentTarget.scrollTop;
  };

  const runCode = () => {
    runCodeHandler(code);
  };

  useEffect(() => {
    updateLines(code);
  }, [code]);

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
        <button className={styles.menu} onClick={showSideBar}>
          <MenuIcon />
        </button>
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
