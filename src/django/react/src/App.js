import React from 'react';
import Header from "./components/Header/Header";
import Main from "./components/Main/Main";
import Footer from "./components/Footer/Footer";
import styles from "./app.module.css";


function App() {
  return (
    <div className={styles.body}>
      <Header />
      <Main />
      <Footer />
    </div>
  );
}

export default App;
