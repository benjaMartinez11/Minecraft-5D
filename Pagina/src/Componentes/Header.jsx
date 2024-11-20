import React from 'react';

const Header = ({ setView }) => {
    return (
        <>
            <header className="header">
                <nav className="navbar">
                    <button className="button" onClick={() => setView("inicio")}>Inicio</button>
                    <button className="button" onClick={() => setView("jugador")}>Jugador</button>
                    <button className="button" onClick={() => setView("mobs")}>Mobs</button>
                    <button className="button" onClick={() => setView("jefes")}>Jefes</button>
                    <button className="button" onClick={() => setView("estructura")}>Estructura</button>
                    <button className="button" onClick={() => setView("dimension")}>Dimensiones</button>
                    <button className="button" onClick={() => setView("agricultura")}>Agricultura</button>
                    <button className="button" onClick={() => setView("cubos")}>Cubos</button>
                </nav>
                <img src="Objetos/Logo-pagina.png" alt="" className="navbar-image bajar" />
            </header>
        </>
    );
};

export default Header;
