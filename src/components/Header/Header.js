import React from 'react';
import styles from './Header.module.css';

function Header() {
  return (
    <header>
      <div className={styles.tituloHeader}>
      Cópia barata do GeoGebra
      </div>
    </header>
  );
}

export default Header;
