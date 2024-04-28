import React from "react";
import Header from "./components/Header/Header";
import styles from "./app.module.css";
import Keyboard from "./components/Keyboard/Keyboard";

function App() {
  return (
    <div className={styles.app}>
      <Header />
      <Keyboard />
    </div>
  );
}

export default App;
