import React from "react";
import Navbar from "./Navbar.jsx";
import "./Header.css";

const Header = () => {
  return (
    <header className="header">
      <div className="header-content">
        <h1>Minecraft 5D</h1>
        <Navbar /> {/* Incluye el Navbar dentro del Header */}
      </div>
    </header>
  );
};

export default Header;
