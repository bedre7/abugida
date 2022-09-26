import React from "react";
import Layout from "../UI/Layout";
import styles from "./Examples.module.scss";
import allExamples from "./examples.json";
import CodeSnippet from "./CodeSnippet";

export interface IExample {
  title: string;
  description: string;
  code: string;
}

const Examples = () => {
  const { examples } = allExamples;

  return (
    <Layout filename="Examples">
      <div className={styles.example}>
        {examples.map((example: IExample, index) => (
          <CodeSnippet key={index} code={example} />
        ))}
      </div>
    </Layout>
  );
};

export default Examples;
