import React from "react";
import styles from "../Solucao/Solucao.module.css";

function Solucao() {
  return (
    <div className={styles.Solucao}>
      <p className={styles.tituloSolucao}></p>
      <p className={styles.respostaSolucao}></p>
    </div>
  );
}

export default Solucao;
