import React, { useContext, MouseEvent } from "react";
import Layout from "../UI/Layout";
import styles from "./Examples.module.scss";
import allExamples from "./examples.json";
import CodeSnippet from "./CodeSnippet";
import { CodeContext, IContext } from "../../context/CodeContext";
import { useNavigate } from "react-router-dom";

export interface IExample {
  title: string;
  description: string;
  code: string;
}

const Examples = () => {
  const { examples } = allExamples;
  const navigate = useNavigate();
  const { setCode, runCodeHandler } = useContext(CodeContext) as IContext;

  const runSnippetHandler = (
    event: MouseEvent<HTMLButtonElement>,
    snippetCode: string
  ) => {
    console.log("In the handler");
    setCode(snippetCode);
    runCodeHandler(snippetCode);
    navigate("/");
  };

  return (
    <Layout filename="Examples">
      <div className={styles.example}>
        {examples.map((example: IExample, index) => (
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
