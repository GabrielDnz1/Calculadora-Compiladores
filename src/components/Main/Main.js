import React from 'react';
import styles from './Main.module.css';

function Main() {
  return (
    <div className={styles.mainBackground}>
      <input className={styles.inputSpace}></input>
      <div className={styles.botoesDosNumeros}>
        <button>1</button>
        <button>2</button>
        <button>3</button>
        <button>4</button>
        <button>5</button>
        <button>6</button>
        <button>7</button>
        <button>8</button>
        <button>9</button>
        <button>0</button>
        <button>𝑥</button>
      </div>
      <div className={styles.botoesMatematica}>
        <button>√</button>
        <button>
          <img src="https://i.imgur.com/U2I8l7X.png" alt=""/>
        </button>
        <button>
          <img src="https://i.imgur.com/EO2ZZFV.png" alt=""/>
        </button>
        <button>
          <img src="https://i.imgur.com/fnYhEKp.png" alt=""/>
        </button>
        <button>
          <img src="https://i.imgur.com/A7AFmJY.png" alt=""/>
        </button>
        <button>
          <img src="https://i.imgur.com/nBNUjX0.png" alt=""/>
        </button>
        <button>
          <img src="https://i.imgur.com/LnHsmy2.png" alt=""/>
        </button>
        <button>
          <img src="https://i.imgur.com/eAUImA8.png" alt=""/>
        </button>
        <button>
          <img src="https://i.imgur.com/QInsGdl.png"/>
        </button>
        <button>y</button>
        <button>ℯ</button>
      </div>
      <div className={styles.botoesMatematicaTerceiraColuna}>
        <button>←</button>
        <button>↑</button>
        <button>→</button>
        <button>+</button>
        <button>-</button>
        <button>x</button>
        <button>÷</button>
        <button>=</button>
        <button>
          <img src="https://i.imgur.com/ByOIU5e.png" alt=""/>
        </button>
        <button>
          <img src="https://i.imgur.com/JOdtMNq.png" alt="" width={"60px"} height={"60px"}/>
        </button>
        <button>√</button>
      </div>
    </div>
  );
}

export default Main;
