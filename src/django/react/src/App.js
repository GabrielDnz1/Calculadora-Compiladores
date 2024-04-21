import React from "react";
import Header from "./Components/Header/Header";
import styles from "./app.module.css";
import Keyboard from "./Components/Keyboard/Keyboard";

function App() {
  return (
    <div className={styles.app}>
      <Header />
      <Keyboard />
    </div>
  );
}

export default App;
