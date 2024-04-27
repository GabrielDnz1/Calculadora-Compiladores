import React, { useEffect, useState } from "react";
import styles from "./Keyboard.module.css";
import AxiosInstance from "../Axios.js";

function Keyboard() {
  const [inputValue, setInputValue] = useState("");
  const [isNumericKeyboard, setIsNumericKeyboard] = useState(false);

  useEffect(() => {
    const handleKeyboardClick = (event) => {
      const target = event.target;
      if (target.tagName === "SPAN") {
        setInputValue((prevValue) => prevValue + target.textContent);
      }
    };

    const base = document.querySelector(`.${styles.base}`);
    base.addEventListener("click", handleKeyboardClick);

    return () => {
      base.removeEventListener("click", handleKeyboardClick);
    };
  }, []);

  function botaoDeEnter() {
    window.scrollTo(0, document.body.scrollHeight);
    
    AxiosInstance.post(`api/backend/`, {
      title: 'expressão',
      content: inputValue
    }).then((response) => {
      console.log(response.data)
    }).catch((error) => {
      console.error("Deu herro hein: ", error)
    });
  }

  function deletaLetra() {
    setInputValue((prevValue) => prevValue.slice(0, -1));
  }

  function MudarKeyboardNumerico() {
    setIsNumericKeyboard((prevValue) => !prevValue);
  }

  function ClearInput() {
    setInputValue("");
  }

  return (
    <div className={styles.input_e_Base}>
      <textarea
        className={styles.Input}
        id="resposta"
        value={inputValue}
        readOnly
      ></textarea>
      <div className={styles.base}>
        <div className={styles.line1}>
          <span className={`${styles.tecla} ${styles.tecla_Q}`}>
            {isNumericKeyboard ? "1" : "Q"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_W}`}>
            {isNumericKeyboard ? "2" : "W"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_E}`}>
            {isNumericKeyboard ? "3" : "E"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_R}`}>
            {isNumericKeyboard ? "4" : "R"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_T}`}>
            {isNumericKeyboard ? "5" : "T"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_Y}`}>
            {isNumericKeyboard ? "6" : "Y"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_U}`}>
            {isNumericKeyboard ? "7" : "U"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_I}`}>
            {isNumericKeyboard ? "8" : "I"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_O}`}>
            {isNumericKeyboard ? "9" : "O"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_P}`}>
            {isNumericKeyboard ? "0" : "P"}
          </span>
        </div>
        <div className={styles.line2}>
          <span className={`${styles.tecla} ${styles.tecla_A}`}>
            {isNumericKeyboard ? "ln" : "A"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_S}`}>
            {isNumericKeyboard ? "sin" : "S"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_D}`}>
            {isNumericKeyboard ? "cos" : "D"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_F}`}>
            {isNumericKeyboard ? "tg" : "F"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_G}`}>
            {isNumericKeyboard ? "√" : "G"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_H}`}>
            {isNumericKeyboard ? "(" : "H"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_J}`}>
            {isNumericKeyboard ? ")" : "J"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_K}`}>
            {isNumericKeyboard ? "{" : "K"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_L}`}>
            {isNumericKeyboard ? "}" : "L"}
          </span>
        </div>
        <div className={styles.line3}>
          <span className={`${styles.tecla} ${styles.tecla_PI}`}>
            {isNumericKeyboard ? "π" : "π"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_Z}`}>
            {isNumericKeyboard ? "+" : "Z"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_X}`}>
            {isNumericKeyboard ? "-" : "X"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_C}`}>
            {isNumericKeyboard ? "×" : "C"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_V}`}>
            {isNumericKeyboard ? "÷" : "V"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_B}`}>
            {isNumericKeyboard ? "," : "B"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_N}`}>
            {isNumericKeyboard ? "^" : "N"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_M}`}>
            {isNumericKeyboard ? "=" : "M"}
          </span>
          <button className={styles.Delete} onClick={deletaLetra}>
            Del
          </button>
        </div>
        <div className={styles.line4}>
          <button className={styles.altnum} onClick={MudarKeyboardNumerico}>
            {isNumericKeyboard ? "ABC" : "123"}
          </button>
          <button className={styles.spacebar} onClick={ClearInput}>
            Clear
          </button>
          <button className={styles.enter} onClick={botaoDeEnter}>
            Solve
          </button>
        </div>
      </div>
    </div>
  );
}

export default Keyboard;
