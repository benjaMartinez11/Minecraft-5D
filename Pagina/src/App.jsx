import React, { useState, useEffect } from "react";
import "./index.css";

const App = () => {
  const [view, setView] = useState("inicio");
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
    // Lista de rutas para obtener los datos desde Flask
    const routes = [
      "jugador",
      "herramientas_basicas",
      "armadura",
      "encantamientos",
      "comida",
      "mob_pass",
      "mob_neutro",
      "mob_hoss",
      "jefes",
      "caracteristicas_jefe",
      "bioma",
      "estructura",
      "dimension",
      "agricultura",
      "cubos",
    ];

    // Fetching de todos los datos
    Promise.all(
      routes.map((route) =>
        fetch(`http://127.0.0.1:5000/${route}`)
          .then((res) => res.json())
          .then((json) => ({ [route]: json }))
      )
    ).then((results) => {
      const newData = results.reduce(
        (acc, current) => ({ ...acc, ...current }),
        {}
      );
      setData(newData);
    });
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
        <h1>Minecraft</h1>
        <img src="/Componentes/Objetos/Site-logo.webp" alt="" className="" />
        <nav className="navbar">
          <button onClick={() => setView("inicio")}>Inicio</button>
          <button onClick={() => setView("jugador")}>Jugador</button>
          <button onClick={() => setView("mobs")}>Mobs</button>
          <button onClick={() => setView("jefes")}>Jefes</button>
          <button onClick={() => setView("biomas")}>Biomas</button>
          <button onClick={() => setView("estructura")}>Estructura</button>
          <button onClick={() => setView("dimension")}>Dimensiones</button>
          <button onClick={() => setView("agricultura")}>Agricultura</button>
          <button onClick={() => setView("cubos")}>Cubos</button>
        </nav>
      </header>

      <main className="body">
        {view === "inicio" && (
          <>
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
          </>
        )}

        {view === "jugador" && (
          <>
            {renderTable("jugador", data.jugador)}
            {renderTable("herramientas_basicas", data.herramientas_basicas)}
            {renderTable("armadura", data.armadura)}
            {renderTable("encantamientos", data.encantamientos)}
          </>
        )}

        {view === "mobs" && (
          <>
            {renderTable("mob_pass", data.mob_pass)}
            {renderTable("mob_neutro", data.mob_neutro)}
            {renderTable("mob_hoss", data.mob_hoss)}
          </>
        )}

        {view === "jefes" && (
          <>
            {renderTable("jefes", data.jefes)}
            {renderTable("caracteristicas_jefe", data.caracteristicas_jefe)}
          </>
        )}

        {view === "biomas" && renderTable("bioma", data.bioma)}
        {view === "estructura" && renderTable("estructura", data.estructura)}
        {view === "dimension" && renderTable("dimension", data.dimension)}
        {view === "agricultura" && renderTable("agricultura", data.agricultura)}
        {view === "cubos" && renderTable("cubos", data.cubos)}
      </main>

      <footer className="footer">
        <p>Creado por X</p>
        <div className="icons">
          <a href="#">Icono 1</a>
          <a href="#">Icono 2</a>
          <a href="#">Icono 3</a>
        </div>
      </footer>
    </>
  );
};

export default App;
