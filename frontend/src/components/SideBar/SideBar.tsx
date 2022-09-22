import React from "react";
import styles from "./SideBar.module.scss";
import { Link } from "react-router-dom";
import { ReactComponent as HomeIcon } from "../../assets/SVG/home.svg";
import { ReactComponent as DocIcon } from "../../assets/SVG/stack.svg";
import { ReactComponent as ExampleIcon } from "../../assets/SVG/clipboard.svg";
import { ReactComponent as Github } from "../../assets/SVG/github.svg";
import { ReactComponent as MailIcon } from "../../assets/SVG/mail4.svg";
import { ReactComponent as LinkedInIcon } from "../../assets/SVG/linkedin.svg";
import { ReactComponent as CodeIcon } from "../../assets/SVG/embed2.svg";

const SideBar = () => {
  return (
    <nav className={styles.sidebar}>
      <header>&lt;Abugida/&gt;</header>
      <ul className={styles.links}>
        <li>
          <Link to="/">
            <HomeIcon />
            <span>Home</span>
          </Link>
        </li>
        <li>
          <Link to="/">
            <DocIcon />
            <span>Documentation</span>
          </Link>
        </li>
        <li>
          <Link to="/">
            <ExampleIcon />
            <span>Examples</span>
          </Link>
        </li>
        <li>
          <Link to="/">
            <CodeIcon />
            <span style={{marginLeft: '.5rem'}}>Source Code</span>
          </Link>
        </li>
      </ul>
      <div className={styles.socials}>
        <ul>
          <li>
            <Link to="/">
              <Github />
            </Link>
          </li>
          <li>
            <Link to="/">
              <MailIcon />
            </Link>
          </li>
          <li>
            <Link to="/">
              <LinkedInIcon />
            </Link>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default SideBar;
