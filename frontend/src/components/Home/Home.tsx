import React, { useContext, FC, Dispatch, SetStateAction } from "react";
import Wrapper from "../UI/Wrapper";
import Editor from "../Editor/Editor";
import styles from "./Home.module.scss";
import Terminal from "../Terminal/Terminal";
import { CodeContext, ICode } from "../../context/CodeContext";

const Home: FC<{ setShowSideBar: Dispatch<SetStateAction<boolean>> }> = ({
  setShowSideBar,
}) => {
  const { setTerminalIsVisible, terminalIsVisible } = useContext(
    CodeContext
  ) as ICode;

  const closeTerminal = () => {
    setTerminalIsVisible(false);
  };

  return (
    <div className={styles.home}>
      <Wrapper>
        <Editor
          isFullSize={!terminalIsVisible}
          showSideBar={() => setShowSideBar((prevState) => !prevState)}
        />
        {terminalIsVisible && <Terminal onClose={closeTerminal} />}
      </Wrapper>
    </div>
  );
};

export default Home;
