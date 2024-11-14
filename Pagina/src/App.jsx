import React, { useState, useEffect } from "react";
import "./index.css";
import { Link } from "react-router-dom";

const App = () => {
  //const [count, setCount] = useState(0)
  const [view, setView] = useState({});

  const [data, setData] = useState({
    jugador: [],
    herramientas_basicas: [],
    armadura: [],
    encantamientos: [],
    comida: [],
    mob_pass: [],
    mob_neutro: [],
    mob_hoss: [],
    jefes: [],
    caracteristicas_jefe: [],
    bioma: [],
    estructura: [],
    dimension: [],
    agricultura: [],
    cubos: [],
  });

  useEffect(() => {
    fetch("http://127.0.0.1:5000/jugador")
      .then((data) => data.json())
      .then((response) => setJugador(response));
    fetch("http://127.0.0.1:5000/herramientas_basicas")
      .then((data) => data.json())
      .then((response) => setHerramientas(response));
    fetch("http://127.0.0.1:5000/armadura")
      .then((data) => data.json())
      .then((response) => setArmadura(response));
    fetch("http://127.0.0.1:5000/encantamientos")
      .then((data) => data.json())
      .then((response) => setEncantamientos(response));
    fetch("http://127.0.0.1:5000/comida")
      .then((data) => data.json())
      .then((response) => setComida(response));
    fetch("http://127.0.0.1:5000/mob_pass")
      .then((data) => data.json())
      .then((response) => setMob_pass(response));
    fetch("http://127.0.0.1:5000/mob_neutro")
      .then((data) => data.json())
      .then((response) => setMob_neutro(response));
    fetch("http://127.0.0.1:5000/mob_hoss")
      .then((data) => data.json())
      .then((response) => setMob_hoss(response));
    fetch("http://127.0.0.1:5000/jefes")
      .then((data) => data.json())
      .then((response) => setJefes(response));
    fetch("http://127.0.0.1:5000/caracteristicas_jefe")
      .then((data) => data.json())
      .then((response) => setCaracteristicas_jefe(response));
    fetch("http://127.0.0.1:5000/bioma")
      .then((data) => data.json())
      .then((response) => setBioma(response));
    fetch("http://127.0.0.1:5000/estructura")
      .then((data) => data.json())
      .then((response) => setEstructura(response));
    fetch("http://127.0.0.1:5000/agricultura")
      .then((data) => data.json())
      .then((response) => setAgricultura(response));
    fetch("http://127.0.0.1:5000/dimension")
      .then((data) => data.json())
      .then((response) => setDimension(response));
    fetch("http://127.0.0.1:5000/cubos")
      .then((data) => data.json())
      .then((response) => setCubos(response));
  }, []);

  const renderTable = (title, items) => (
    <div className="table-section" id={title}>
      <h2>{title}</h2>
      <table>
        <thead>
          <tr>
            {items.length > 0 &&
              Object.keys(items[0]).map((key) => <th key={key}>{key}</th>)}
          </tr>
        </thead>
        <tbody>
          {items.map((item, index) => (
            <tr key={index}>
              {Object.values(item).map((value, idx) => (
                <td key={idx}>{value}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );

  return (
    <>
      <header className="header">
        <p>Minecraft</p>
        <nav className="navbar">
          <button onClick={() => setView("inicio")}></button>
          <button onClick={() => setView("jugador")}></button>
          <button onClick={() => setView("mobs")}></button>
          <button onClick={() => setView("jefes")}></button>
          <button onClick={() => setView("biomas")}></button>
          <button onClick={() => setView("estructura")}></button>
          <button onClick={() => setView("dimension")}></button>
          <button onClick={() => setView("agricultura")}></button>
          <button onClick={() => setView("cubos")}></button>
        </nav>
      </header>

      <main>
        {view === "inicio" && (
          <main className="body">
            {renderTable("jugador", data.jugador)}
            {renderTable("herramientas_basicas", data.herramientas_basicas)}
            {renderTable("armadura", data.armadura)}
            {renderTable("encantamientos", data.encantamientos)}
            {renderTable("comida", data.comida)}
            {renderTable("mob_pass", data.mob_pass)}
            {renderTable("mob_neutro", data.mob_neutro)}
            {renderTable("mob_hoss", data.mob_hoss)}
            {renderTable("jefes", data.jefes)}
            {renderTable("caracteristicas_jefe", data.caracteristicas_jefe)}
            {renderTable("bioma", data.bioma)}
            {renderTable("estructura", data.estructura)}
            {renderTable("dimension", data.dimension)}
            {renderTable("agricultura", data.agricultura)}
            {renderTable("cubos", data.cubos)}
          </main>
        )}

        {view === "jugador" && (
          <main className="body">
            {renderTable("jugador", data.jugador)}
            {renderTable("herramientas_basicas", data.herramientas_basicas)}
            {renderTable("armadura", data.armadura)}
            {renderTable("encantamientos", data.encantamientos)}
          </main>
        )}

        {view === "mobs" && (
          <main className="body">
            {renderTable("mob_pass", data.mob_pass)}
            {renderTable("mob_neutro", data.mob_neutro)}
            {renderTable("mob_hoss", data.mob_hoss)}
          </main>
        )}

        {view === "jefes" && (
          <main className="body">
            {renderTable("jefes", data.jefes)}
            {renderTable("caracteristicas_jefe", data.caracteristicas_jefe)}
          </main>
        )}

        {view === "biomas" && (
          <main className="body">{renderTable("bioma", data.bioma)}</main>
        )}

        {view === "estructura" && (
          <main className="body">
            {renderTable("estructura", data.estructura)}
          </main>
        )}

        {view === "dimension" && (
          <main className="body">
            {renderTable("dimension", data.dimension)}
          </main>
        )}

        {view === "agricultura" && (
          <main className="body">
            {renderTable("agricultura", data.agricultura)}
          </main>
        )}

        {view === "cubos" && (
          <main className="body">{renderTable("cubos", data.cubos)}</main>
        )}
      </main>

      <footer className="footer">
        <p>Creado por X</p>
        <div className="icons">
          <a href=""></a>
          <a href=""></a>
          <a href=""></a>
        </div>
      </footer>
    </>
  );
};

export default App;
