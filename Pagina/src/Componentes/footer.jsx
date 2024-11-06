// Footer.js
import React from 'react';
import { FaGithub, FaYoutube, FaInstagramSquare } from 'react-icons/fa';
import '../index.css';

function Footer() {
  return (
    <footer className="footer">
      <p>&copy; {new Date().getFullYear()} - Hecho por Mico0102, iPanditaC_ y Benja_vc</p>
      <div className="social-icons">
        <a href="https://www.youtube.com/" target="_blank" rel="noopener noreferrer">
          <FaYoutube size={30} />
        </a>
        <a href="https://github.com/" target="_blank" rel="noopener noreferrer">
          <FaGithub size={30} />
        </a>
        <a href="https://www.instagram.com/" target="_blank" rel="noopener noreferrer">
          <FaInstagramSquare size={30} />
        </a>
      </div>
    </footer>
  );
}

export default Footer;
