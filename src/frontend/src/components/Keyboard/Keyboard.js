import React, { useEffect, useState } from "react";
import styles from "./Keyboard.module.css";
import AxiosInstance from "../Axios.js";

function Keyboard() {
  const [inputValue, setInputValue] = useState("");
  const [isNumericKeyboard, setIsNumericKeyboard] = useState(false);
  const [isPopupOpen, setIsPopupOpen] = useState(false);
  const [resultado, setResultado] = useState(null);
  const [isShiftPressed, setIsShiftPressed] = useState(false);

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
    setIsPopupOpen(true);
    AxiosInstance.post(`api/backend/`, {
      title: "expressão",
      content: inputValue,
    })
      .then((response) => {
        console.log(response.data);
        setResultado(response.data);
      })
      .catch((error) => {
        console.error("Deu herro hein: ", error);
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

  function handleShiftPress() {
    setIsShiftPressed((prevValue) => !prevValue);
    var botao = document.getElementById("shiftButton");
    var cordeBackground1 = "#2f3336";
    var cordeBackground2 = "#FFFFFF";

    if (botao.style.backgroundColor == cordeBackground1) {
      botao.style.backgroundColor = cordeBackground2;
    } else {
      botao.style.backgroundColor = cordeBackground1;
    }
  }

  function handlePopupClose() {
    setIsPopupOpen(false);
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
            {isNumericKeyboard ? "1" : isShiftPressed ? "Q" : "q"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_W}`}>
            {isNumericKeyboard ? "2" : isShiftPressed ? "W" : "w"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_E}`}>
            {isNumericKeyboard ? "3" : isShiftPressed ? "E" : "e"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_R}`}>
            {isNumericKeyboard ? "4" : isShiftPressed ? "R" : "r"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_T}`}>
            {isNumericKeyboard ? "5" : isShiftPressed ? "T" : "t"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_Y}`}>
            {isNumericKeyboard ? "6" : isShiftPressed ? "Y" : "y"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_U}`}>
            {isNumericKeyboard ? "7" : isShiftPressed ? "U" : "u"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_I}`}>
            {isNumericKeyboard ? "8" : isShiftPressed ? "I" : "i"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_O}`}>
            {isNumericKeyboard ? "9" : isShiftPressed ? "O" : "o"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_P}`}>
            {isNumericKeyboard ? "0" : isShiftPressed ? "P" : "p"}
          </span>
        </div>
        <div className={styles.line2}>
          <span className={`${styles.tecla} ${styles.tecla_A}`}>
            {isNumericKeyboard ? "ln" : isShiftPressed ? "A" : "a"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_S}`}>
            {isNumericKeyboard ? "sin" : isShiftPressed ? "S" : "s"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_D}`}>
            {isNumericKeyboard ? "cos" : isShiftPressed ? "D" : "d"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_F}`}>
            {isNumericKeyboard ? "tg" : isShiftPressed ? "F" : "f"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_G}`}>
            {isNumericKeyboard ? "√" : isShiftPressed ? "G" : "g"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_H}`}>
            {isNumericKeyboard ? "(" : isShiftPressed ? "H" : "h"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_J}`}>
            {isNumericKeyboard ? ")" : isShiftPressed ? "J" : "j"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_K}`}>
            {isNumericKeyboard ? "{" : isShiftPressed ? "K" : "k"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_L}`}>
            {isNumericKeyboard ? "}" : isShiftPressed ? "L" : "l"}
          </span>
        </div>
        <div className={styles.line3}>
          <button
            className={`${styles.tecla_shift} ${
              isShiftPressed ? styles.shiftPressed : ""
            }`}
            onClick={handleShiftPress}
            id="shiftButton"
          >
            {isNumericKeyboard ? "⇧" : "⇧"}
          </button>
          <span className={`${styles.tecla} ${styles.tecla_PI}`}>
            {isNumericKeyboard ? "π" : "π"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_Z}`}>
            {isNumericKeyboard ? "+" : isShiftPressed ? "Z" : "z"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_X}`}>
            {isNumericKeyboard ? "-" : isShiftPressed ? "X" : "x"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_C}`}>
            {isNumericKeyboard ? "x" : isShiftPressed ? "C" : "c"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_V}`}>
            {isNumericKeyboard ? "÷" : isShiftPressed ? "V" : "v"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_B}`}>
            {isNumericKeyboard ? "," : isShiftPressed ? "B" : "b"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_N}`}>
            {isNumericKeyboard ? "^" : isShiftPressed ? "N" : "n"}
          </span>
          <span className={`${styles.tecla} ${styles.tecla_M}`}>
            {isNumericKeyboard ? "=" : isShiftPressed ? "M" : "m"}
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
      {isPopupOpen && (
        <div className={styles.popup}>
          <h1>SOLUÇÃO</h1>
          <h1 className={styles.valordoinput}>{resultado}</h1>
          <a className={styles.close} href="#" onClick={handlePopupClose}>
            CLOSE
          </a>
        </div>
      )}
    </div>
  );
}

export default Keyboard;
