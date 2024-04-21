import React from 'react';
import styles from './Main.module.css';

function Main() {
    const digitarNumero = (botao) => {
      let resposta = document.getElementById('resposta');
      if (resposta.innerHTML === "Digite pelos botões abaixo") {
        resposta.innerHTML = "";
      }
      resposta.innerHTML += botao;
    }
  
  const deletarNumero = () => {
    const resposta = document.getElementById('resposta');
    resposta.innerHTML = resposta.innerHTML.slice(0, -1);
  }


  return (
    <div className={styles.mainBackground}>
      <h1 className={styles.resposta} id='resposta'>Digite pelos botões abaixo</h1>
      <div className={styles.keyboardspace}>
        <div className={styles.botoesPrimeiraColuna}>
            <button onClick={() => digitarNumero('1')}>1</button>
            <button onClick={() => digitarNumero('2')}>2</button>
            <button onClick={() => digitarNumero('3')}>3</button>
            <button onClick={() => digitarNumero('𝑥')}>𝑥</button>
            <button onClick={() => digitarNumero('y')}>y</button>
            <button onClick={() => digitarNumero('z')}>z</button>
            <button onClick={() => digitarNumero('ℯ')}>ℯ</button>
            <button onClick={() => digitarNumero('α')}>α</button>
            <button onClick={() => digitarNumero('β')}>β</button>
            <button onClick={() => digitarNumero('Δ')}>Δ</button>
          </div>
      <div className={styles.botoesSegundaColuna}>
        <button onClick={() => digitarNumero('4')}>4</button>
        <button onClick={() => digitarNumero('5')}>5</button>
        <button onClick={() => digitarNumero('6')}>6</button>
        <button>
          <img src='https://i.imgur.com/ZE22ZQH.png' alt='' width={"80px"} draggable="false"/>
        </button>
        <button>
          <img src='https://i.imgur.com/1aWHnD5.png' alt='' width={"80px"} draggable="false"/>
        </button>
        <button>
          <img src='https://i.imgur.com/rYA2vYc.png' alt='' width={"80px"} draggable="false"/>
          
        </button>
        <button>
          <img src='https://i.imgur.com/mDDLlSJ.png' alt='' width={"80px"} draggable="false"/>
        </button>
        <button>
          <img src='https://i.imgur.com/qoTU2YV.png' alt='' width={"80px"} draggable="false" onClick={() => digitarNumero('√')}/>
        </button>
        <button>
          <img src='https://i.imgur.com/cNZDfW5.png' alt='' width={"80px"} draggable="false" onClick={() => digitarNumero('<')}/>
        </button>
        <button>
          <img src='https://i.imgur.com/igBmjn6.png' alt='' width={"80px"} draggable="false" onClick={() => digitarNumero('>')}/>
        </button>
      </div>
      <div className={styles.botoesTerceiraColuna}>
        <button onClick={() => digitarNumero('7')}>7</button>
        <button onClick={() => digitarNumero('8')}>8</button>
        <button onClick={() => digitarNumero('9')}>9</button>
        <button className={styles.btnSeta}>↑</button>
        <button>
          <img src='https://i.imgur.com/cZiqJWw.png' alt='' width={"80px"} draggable="false" onClick={() => digitarNumero('(')}/>
        </button>
        <button>
          <img src='https://i.imgur.com/IlxUTlW.png' alt='' width={"80px"} draggable="false" onClick={() => digitarNumero(')')}/>
        </button>
        <button className={styles.arcos} onClick={() => digitarNumero('ln(')}>ln</button>
        <button className={styles.arcos} onClick={() => digitarNumero('sen(')}>sen</button>
        <button className={styles.arcos} onClick={() => digitarNumero('cos(')}>cos</button>
        <button className={styles.arcos} onClick={() => digitarNumero('tg(')}>tan</button>
      </div>
      <div className={styles.botoesQuartaColuna}>
        <button onClick={() => digitarNumero(',')}>,</button>
        <button onClick={() => digitarNumero('0')}>0</button>
        <button className={styles.btnSeta}>←</button>
        <button className={styles.btnSeta}>↓</button>
        <button className={styles.btnSeta}>→</button>
        <button onClick={() => digitarNumero('+')}>+</button>
        <button onClick={() => digitarNumero('-')}>-</button>
        <button onClick={() => digitarNumero('*')}>x</button>
        <button onClick={() => digitarNumero('÷')}>÷</button>
        <button onClick={() => deletarNumero()}>
          <img src='https://i.imgur.com/JOdtMNq.png' alt='' width={"45px"} draggable="false"/>
        </button>
      </div>
    </div>
</div>
    
  );
}

export default Main;