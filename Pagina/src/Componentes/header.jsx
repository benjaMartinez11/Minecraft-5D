// Header.js
import React from 'react';
import "../index.css"

function Header() {
  return (
    <header className="header">
      <img src="./public/imagens/minecraftlogoo.png" alt="Logo" className="header-logo" />
      <nav className="nav">
        <ul className="nav-list">
          <li><a href="#home">Inicio</a></li>
          <li><a href="#about">Acerca de</a></li>
          <li><a href="#services">Servicios</a></li>
          <li><a href="#contact">Contacto</a></li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;
