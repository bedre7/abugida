import React, { useState, FC } from "react";
import { ReactComponent as MenuIcon } from "../../assets/SVG/menu.svg";
import { ReactComponent as CloseIcon } from "../../assets/SVG/cross.svg";
import styles from "./MenuBar.module.scss";

const MenuBar: FC<{ onClose: () => void }> = ({ onClose }) => {
  const [menuIsClosed, setMenuIsClosed] = useState(true);

  const clickHandler = () => {
    setMenuIsClosed((prevState) => !prevState);
    onClose();
  };

  return (
    <button className={styles.menu} onClick={clickHandler}>
      {!menuIsClosed ? <MenuIcon /> : <CloseIcon />}
    </button>
  );
};

export default MenuBar;
