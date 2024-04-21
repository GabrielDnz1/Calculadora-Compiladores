import React, { useEffect } from "react";
import styles from "./Keyboard.module.css";

function Keyboard() {
  useEffect(() => {
    const base = document.querySelector(`.${styles.base}`);
    base.onclick = function (event) {
      const target = event.target;
      if (target.tagName === "SPAN") {
        const resposta = document.getElementById("resposta");
        if (resposta.innerHTML === "Digite pelos botões abaixo") {
          resposta.innerHTML = "";
        }
        resposta.innerHTML += target.textContent;
      }
    };
  }, []);

  return (
    <div className={styles.input_e_Base}>
      <textarea className={styles.Input} id="resposta"></textarea>
      <div className={styles.base}>
        <div className={styles.line1}>
          <span className={styles.tecla_Q}>Q</span>
          <span className={styles.tecla_W}>W</span>
          <span className={styles.tecla_E}>E</span>
          <span className={styles.tecla_Y}>Y</span>
          <span className={styles.tecla_U}>U</span>
          <span className={styles.tecla_I}>I</span>
          <span className={styles.tecla_O}>O</span>
          <span className={styles.tecla_P}>P</span>
        </div>
        <div className={styles.line2}>
          <span className={styles.tecla_A}>A</span>
          <span className={styles.tecla_S}>S</span>
          <span className={styles.tecla_D}>D</span>
          <span className={styles.tecla_F}>F</span>
          <span className={styles.tecla_G}>G</span>
          <span className={styles.tecla_H}>H</span>
          <span className={styles.tecla_J}>J</span>
          <span className={styles.tecla_K}>K</span>
          <span className={styles.tecla_L}>L</span>
        </div>
        <div className={styles.line3}>
          <span className={styles.tecla_PI}>π</span>
          <span className={styles.tecla_Z}>Z</span>
          <span className={styles.tecla_X}>X</span>
          <span className={styles.tecla_C}>C</span>
          <span className={styles.tecla_V}>V</span>
          <span className={styles.tecla_B}>B</span>
          <span className={styles.tecla_N}>N</span>
          <span className={styles.tecla_M}>M</span>
          <span className={styles.tecla_Delete}>Del</span>
        </div>
        <div className={styles.line4}>
          <span className={styles.altnum}>123</span>
          <span className={styles.spacebar}>Space</span>
          <span className={styles.enter}>Enter</span>
        </div>
      </div>
    </div>
  );
}

export default Keyboard;
