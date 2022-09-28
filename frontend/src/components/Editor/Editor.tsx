import React, {
  ChangeEvent,
  useContext,
  useRef,
  useEffect,
  useCallback,
  FC,
} from "react";
import Layout from "../UI/Layout";
import styles from "./Editor.module.scss";
import { CodeContext, ICode } from "../../context/CodeContext";

interface EditorProps {
  isFullSize: boolean;
}

const Editor: FC<EditorProps> = ({ isFullSize }) => {
  const lineBarRef = useRef<HTMLDivElement>(null);
  const { code, lines, setCode, setLines, runCodeHandler } = useContext(
    CodeContext
  ) as ICode;

  const updateLines = useCallback(
    (value: string) => {
      if (value === "") setLines([1]);
      else {
        const numberOfLines = value.split(/\r*\n/).length;
        setLines([]);
        for (let i = 1; i <= numberOfLines; i++) {
          setLines((prevLines) => Array.from(new Set([...prevLines, i])));
        }
      }
    },
    [setLines]
  );

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
  }, [code, updateLines]);

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
