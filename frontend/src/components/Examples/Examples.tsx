import { useNavigate } from "react-router-dom";
import React, { useContext, MouseEvent } from "react";
import Layout from "../UI/Layout";
import CodeSnippet from "./CodeSnippet";
import allExamples from "./examples.json";
import styles from "./Examples.module.scss";
import { CodeContext, ICode } from "../../context/CodeContext";

export interface IExample {
  title: string;
  description: string;
  codes: string[];
}

const Examples = () => {
  const { examples } = allExamples;
  const navigate = useNavigate();
  const { setCode, runCodeHandler } = useContext(CodeContext) as ICode;

  const runSnippetHandler = (
    event: MouseEvent<HTMLButtonElement>,
    snippetCode: string[]
  ) => {
    setCode((code) => snippetCode.join("\n"));
    runCodeHandler(snippetCode.join("\n"));
    navigate("/");
  };

  return (
    <Layout filename="Examples">
      <div className={styles.example}>
        {examples.map((example:IExample, index) => (
          <CodeSnippet
            key={index}
            code={example}
            onRunSnippet={runSnippetHandler}
          />
        ))}
      </div>
    </Layout>
  );
};

export default Examples;
