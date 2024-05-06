import React, { useEffect, useState } from "react";
import styles from "./Keyboard.module.css";
import AxiosInstance from "../Axios.js";

function Keyboard() {
  const [inputValue, setInputValue] = useState("");
  const [isNumericKeyboard, setIsNumericKeyboard] = useState(true);
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
  }

  function handlePopupClose() {
    setIsPopupOpen(false);
  }

  function handleInputChange(event){
    setInputValue(event.target.value)
  }

  const calculusKeyboard = 

  <div className={`${styles.keyboard} ${styles.calculus}`}>
    <div className={`${styles.part}`}>
      <div className={`${styles.line}`}>
        <span className={`${styles.tecla}`}>{"+"}</span>
        <span className={`${styles.tecla}`}>{"-"}</span>
        <span className={`${styles.tecla}`}>{"*"}</span>
        <span className={`${styles.tecla}`}>{"/"}</span>
        <span className={`${styles.tecla}`}>{"="}</span>
      </div>
      <div className={`${styles.line}`}>
        <span className={`${styles.tecla}`}>{"x"}</span>
        <span className={`${styles.tecla}`}>{"7"}</span>
        <span className={`${styles.tecla}`}>{"8"}</span>
        <span className={`${styles.tecla}`}>{"9"}</span>
        <span className={`${styles.tecla}`}>{"("}</span>
      </div>
      <div className={`${styles.line}`}>
        <span className={`${styles.tecla}`}>{"y"}</span>
        <span className={`${styles.tecla}`}>{"4"}</span>
        <span className={`${styles.tecla}`}>{"5"}</span>
        <span className={`${styles.tecla}`}>{"6"}</span>
        <span className={`${styles.tecla}`}>{")"}</span>
      </div>
      <div className={`${styles.line}`}>
        <span className={`${styles.tecla}`}>{"z"}</span>
        <span className={`${styles.tecla}`}>{"1"}</span>
        <span className={`${styles.tecla}`}>{"2"}</span>
        <span className={`${styles.tecla}`}>{"3"}</span>
        <span className={`${styles.tecla}`}>{"^"}</span>
      </div>
      <div className={`${styles.line}`}>
        <button className={styles.altnum} onClick={MudarKeyboardNumerico}>{"ABC"}</button>
        <span className={`${styles.tecla}`}>{","}</span>
        <span className={`${styles.tecla}`}>{"0"}</span>
        <span className={`${styles.tecla}`}>{"."}</span>
        <button className={styles.enter} onClick={botaoDeEnter}>←</button>
      </div>
    </div>
    <div className={`${styles.part}`}>
      <div className={`${styles.line}`}>
        <span className={`${styles.tecla}`}>{"sin"}</span>
        <span className={`${styles.tecla}`}>{"ln"}</span>
        <span className={`${styles.tecla}`}>{"lim"}</span>
      </div>
      <div className={`${styles.line}`}>
        <span className={`${styles.tecla}`}>{"cos"}</span>
        <span className={`${styles.tecla}`}>{"log"}</span>
        <span className={`${styles.tecla}`}>{"'"}</span>
      </div>
      <div className={`${styles.line}`}>
        <span className={`${styles.tecla}`}>{"tg"}</span>
        <span className={`${styles.tecla}`}>{"√"}</span>
        <span className={`${styles.tecla}`}>{"∫"}</span>
      </div>
      <div className={`${styles.line}`}>
        <span className={`${styles.tecla}`}>{"π"}</span>
        <span className={`${styles.tecla}`}>{"e"}</span>
        <span className={`${styles.tecla}`}>{"Δ"}</span>
      </div>
      <div className={`${styles.line}`}>
        <button className={styles.delete} onClick={deletaLetra}>Del</button>
        <button className={styles.spacebar} onClick={ClearInput}>Clear</button>
      </div>
    </div>
  </div>

  const alphabeticKeyboard =

  <div className={`${styles.keyboard} ${styles.alpha}`}>
    <div className={`${styles.part}`}>
      <div className={`${styles.line}`}>
        <span className={`${styles.tecla}`}>{"α"}</span>
        <span className={`${styles.tecla}`}>{"β"}</span>
        <span className={`${styles.tecla}`}>{"γ"}</span>
        <span className={`${styles.tecla}`}>{"Δ"}</span>
        <span className={`${styles.tecla}`}>{"θ"}</span>
        <span className={`${styles.tecla}`}>{"λ"}</span>
        <span className={`${styles.tecla}`}>{"σ"}</span>
        <span className={`${styles.tecla}`}>{"τ"}</span>
        <span className={`${styles.tecla}`}>{"φ"}</span>
        <span className={`${styles.tecla}`}>{"ω"}</span>
      </div>
      <div className={`${styles.line}`}>
        <span className={`${styles.tecla}`}>{isShiftPressed ? "Q" : "q"}</span>
        <span className={`${styles.tecla}`}>{isShiftPressed ? "W" : "w"}</span>
        <span className={`${styles.tecla}`}>{isShiftPressed ? "E" : "e"}</span>
        <span className={`${styles.tecla}`}>{isShiftPressed ? "R" : "r"}</span>
        <span className={`${styles.tecla}`}>{isShiftPressed ? "T" : "t"}</span>
        <span className={`${styles.tecla}`}>{isShiftPressed ? "Y" : "y"}</span>
        <span className={`${styles.tecla}`}>{isShiftPressed ? "U" : "u"}</span>
        <span className={`${styles.tecla}`}>{isShiftPressed ? "I" : "i"}</span>
        <span className={`${styles.tecla}`}>{isShiftPressed ? "O" : "o"}</span>
        <span className={`${styles.tecla}`}>{isShiftPressed ? "P" : "p"}</span>
      </div>
      <div className={`${styles.line}`}>
      <span className={`${styles.tecla}`}>{isShiftPressed ? "A" : "a"}</span>
        <span className={`${styles.tecla}`}>{isShiftPressed ? "S" : "s"}</span>
        <span className={`${styles.tecla}`}>{isShiftPressed ? "D" : "d"}</span>
        <span className={`${styles.tecla}`}>{isShiftPressed ? "F" : "f"}</span>
        <span className={`${styles.tecla}`}>{isShiftPressed ? "G" : "g"}</span>
        <span className={`${styles.tecla}`}>{isShiftPressed ? "H" : "h"}</span>
        <span className={`${styles.tecla}`}>{isShiftPressed ? "J" : "j"}</span>
        <span className={`${styles.tecla}`}>{isShiftPressed ? "K" : "k"}</span>
        <span className={`${styles.tecla}`}>{isShiftPressed ? "L" : "l"}</span>
        <span className={`${styles.tecla}`}>{isShiftPressed ? "Ç" : "ç"}</span>
      </div>
      <div className={`${styles.line}`}>
        <button className={`${styles.tecla_shift} ${isShiftPressed ? styles.shiftPressed : ""}`} onClick={handleShiftPress} id="shiftButton">
          {"⇧"}
        </button>
        <span className={`${styles.tecla}`}>{isShiftPressed ? "Z" : "z"}</span>
        <span className={`${styles.tecla}`}>{isShiftPressed ? "X" : "x"}</span>
        <span className={`${styles.tecla}`}>{isShiftPressed ? "C" : "c"}</span>
        <span className={`${styles.tecla}`}>{isShiftPressed ? "V" : "v"}</span>
        <span className={`${styles.tecla}`}>{isShiftPressed ? "B" : "b"}</span>
        <span className={`${styles.tecla}`}>{isShiftPressed ? "N" : "n"}</span>
        <span className={`${styles.tecla}`}>{isShiftPressed ? "M" : "m"}</span>
        <button className={styles.enter} onClick={botaoDeEnter}>←</button>
      </div>
      <div className={`${styles.line}`}>
        <button className={styles.altnum} onClick={MudarKeyboardNumerico}>{"123"}</button>
        <button className={styles.delete} onClick={deletaLetra}>Del</button>
        <button className={styles.spacebar} onClick={ClearInput}>Clear</button>
      </div>
    </div>
  </div>

  return (
    <div className={styles.input_e_Base}>
      <textarea
        className={styles.Input}
        id="resposta"
        value={inputValue}
        onChange={handleInputChange}
      ></textarea>
      <div className={styles.base}>  
        {isNumericKeyboard ? calculusKeyboard: alphabeticKeyboard}
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