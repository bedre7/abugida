import React, { ReactNode, FC } from "react";
import styles from "./Layout.module.scss";
import { ReactComponent as TerminalIcon } from "../../assets/SVG/terminal.svg";
import { ReactComponent as FileIcon } from "../../assets/SVG/file.svg";
import { ReactComponent as RunIcon } from "../../assets/SVG/play3.svg";
import { ReactComponent as CloseIcon } from "../../assets/SVG/cancel-circle.svg";

interface LayoutProps {
  filename: string;
  element?: string;
  buttonType?: string;
  children: ReactNode;
  text?: string;
  clickHandler?: (event: React.MouseEvent<HTMLButtonElement>) => void;
}
const Layout: FC<LayoutProps> = ({
  children,
  filename,
  element,
  buttonType,
  text,
  clickHandler
}) => {
  return (
    <div
      className={`${styles.layout} ${
        element === "terminal" ? styles.terminal : ""
      }`}
    >
      <div className={styles.topbar}>
        <div className={styles.filename}>
          {element === "terminal" ? <TerminalIcon /> : <FileIcon />}
          <span>{filename}</span>
        </div>
        <button className={styles.control} onClick={clickHandler}>
          {buttonType === "run" ? <RunIcon /> : <CloseIcon />}{text}
        </button>
      </div>
      {children}
    </div>
  );
};

export default Layout;
