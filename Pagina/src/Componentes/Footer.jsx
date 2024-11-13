import React from "react";
import "../index.css";

const Footer = () => {
  return (
    <footer className="footer">
      <p>Creado por Coronel, Martinez y Corbalan</p>
      <div className="icons">
        <a
          href="https://facebook.com"
          target="_blank"
          rel="noopener noreferrer"
        >
          <i className="fab fa-facebook"></i> {/* Icono de Facebook */}
        </a>
        <a href="https://twitter.com" target="_blank" rel="noopener noreferrer">
          <i className="fab fa-twitter"></i> {/* Icono de Twitter */}
        </a>
        <a
          href="https://instagram.com"
          target="_blank"
          rel="noopener noreferrer"
        >
          <i className="fab fa-instagram"></i> {/* Icono de Instagram */}
        </a>
      </div>
    </footer>
  );
};

export default Footer;
