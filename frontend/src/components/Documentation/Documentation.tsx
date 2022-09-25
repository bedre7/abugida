import React from "react";
import styles from "./Documentation.module.scss";
import Layout from "../UI/Layout";
import documentation from "./docs.json";
import ListItem from "../UI/ListItem";

const Documentation = () => {
  const { docs } = documentation;
  return (
    <Layout filename="Documentation">
      <div className={styles.documentation}>
        {docs.map((docItem: any, index) => (
          <ListItem key={index} item={docItem} />
        ))}
      </div>
    </Layout>
  );
};

export default Documentation;
