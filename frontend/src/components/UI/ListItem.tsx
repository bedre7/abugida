import React, { FC } from "react";
import styles from "./ListItem.module.scss";
import { ReactComponent as ArrowIcon } from "../../assets/SVG/forward.svg";

interface Item {
  title: string;
  description: string;
  details: string[];
}

const ListItem: FC<{ item: Item }> = ({ item }) => {
  return (
    <div className={styles.item}>
      <div className={styles.title}>
        <ArrowIcon />
        <p>{item.title}</p>
      </div>
      <p className={styles.description}>{item.description}</p>
      <ul className={styles.list}>
        {item.details.map((detail: string, index: number) => (
          <li key={index}>{detail}</li>
        ))}
      </ul>
    </div>
  );
};

export default ListItem;
