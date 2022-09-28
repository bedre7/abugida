import React from "react";
import styles from "./SideBar.module.scss";
import { NavLink } from "react-router-dom";
import { ReactComponent as HomeIcon } from "../../assets/SVG/home.svg";
import { ReactComponent as AboutIcon } from "../../assets/SVG/rocket.svg";
import { ReactComponent as DocIcon } from "../../assets/SVG/stack.svg";
import { ReactComponent as ExampleIcon } from "../../assets/SVG/clipboard.svg";
import { ReactComponent as Github } from "../../assets/SVG/github.svg";
import { ReactComponent as MailIcon } from "../../assets/SVG/mail4.svg";
import { ReactComponent as LinkedInIcon } from "../../assets/SVG/linkedin.svg";
import { ReactComponent as CodeIcon } from "../../assets/SVG/embed2.svg";

const setStyle = ({ isActive }: { isActive: boolean }) =>
  isActive ? styles.active : "";

const SideBar = () => {
  return (
    <nav className={styles.sidebar}>
      <header>&lt;Abugida/&gt;</header>
      <ul className={styles.links}>
        <li>
          <NavLink to="/" className={setStyle}>
            <HomeIcon />
            <span>Home</span>
          </NavLink>
        </li>
        <li>
          <NavLink to="/About" className={setStyle}>
            <AboutIcon />
            <span>About</span>
          </NavLink>
        </li>
        <li>
          <NavLink to="/Documentation" className={setStyle}>
            <DocIcon />
            <span>Documentation</span>
          </NavLink>
        </li>
        <li>
          <NavLink to="/Examples" className={setStyle}>
            <ExampleIcon />
            <span>Examples</span>
          </NavLink>
        </li>
        <li>
          <a href="https://github.com/bedre7/abugida" target="blank">
            <CodeIcon />
            <span style={{ marginLeft: "1.5rem" }}>Source Code</span>
          </a>
        </li>
      </ul>
      <div className={styles.socials}>
        <ul>
          <li>
            <a href="https://github.com/bedre7" target="blank">
              <Github />
            </a>
          </li>
          <li>
            <a href="mailto:bedru777@gmail.com" target="blank">
              <MailIcon />
            </a>
          </li>
          <li>
            <a href="https://www.linkedin.com/in/bedru-umer/" target="blank">
              <LinkedInIcon />
            </a>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default SideBar;
