import React from "react";
import styles from "./About.module.scss";
import Layout from "../UI/Layout";

const About = () => {
  return (
    <Layout filename="About">
      <div className={styles.about}>
        <h1>Abugida(አቡጊዳ)</h1>
        <p>
          Abugida(አቡጊዳ) is high-level programming language supporting basic data
          types with a built-in Lexer, Parser, Interpreter and Abstract Syntax
          Tree. It is implemented in python with a simple syntax.
        </p>
      </div>
    </Layout>
  );
};

export default About;
