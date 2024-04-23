import React from "react";
import Header from "./components/Header/Header";
import styles from "./app.module.css";
import Keyboard from "./components/Keyboard/Keyboard";
import Solucao from "./components/Solucao/Solucao";

function App() {
  return (
    <div className={styles.app}>
      <Header />
      <Keyboard />
      <Solucao />
    </div>
  );
}

export default App;
