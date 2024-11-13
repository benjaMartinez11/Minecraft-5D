import React, { useState } from "react";
import "./index.css";
import Header from "./Componentes/Header";
import Navbar from "./Componentes/Navbar";
import Footer from "./Componentes/Footer";

function App() {

  //const [count, setCount] = useState(0)
const MinecraftPage = () => {
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
      .then((response) => setPartidos1(response));
    fetch("http://127.0.0.1:5000/herramientas_basicas")
      .then((data) => data.json())
      .then((response) => setPartidos2(response));
    fetch("http://127.0.0.1:5000/armadura")
      .then((data) => data.json())
      .then((response) => setPartidos2(response));
    fetch("http://127.0.0.1:5000/encantamientos")
      .then((data) => data.json())
      .then((response) => setPartidos2(response));
    fetch("http://127.0.0.1:5000/comida")
      .then((data) => data.json())
      .then((response) => setPuntos1(response));
    fetch("http://127.0.0.1:5000/mob_pass")
      .then((data) => data.json())
      .then((response) => setPuntos2(response));
    fetch("http://127.0.0.1:5000/mob_neutro")
      .then((data) => data.json())
      .then((response) => setPuntos2(response));
    fetch("http://127.0.0.1:5000/mob_hoss")
      .then((data) => data.json())
      .then((response) => setPuntos2(response));
    fetch("http://127.0.0.1:5000/jefes")
      .then((data) => data.json())
      .then((response) => setPuntos(response));
    fetch("http://127.0.0.1:5000/caracteristicas_jefe")
      .then((data) => data.json())
      .then((response) => setPartidos2(response));
    fetch("http://127.0.0.1:5000/bioma")
      .then((data) => data.json())
      .then((response) => setPuntos(response));
    fetch("http://127.0.0.1:5000/estructura")
      .then((data) => data.json())
      .then((response) => setPartidos2(response));
    fetch("http://127.0.0.1:5000/agricultura")
      .then((data) => data.json())
      .then((response) => setPuntos(response));
    fetch("http://127.0.0.1:5000/dimension")
      .then((data) => data.json())
      .then((response) => setPuntos(response));
    fetch("http://127.0.0.1:5000/cubos")
      .then((data) => data.json())
      .then((response) => setPartidos2(response));
  }, []);

  return (
    <>
      <div>
        <header className="header">
          <p>Minecraft</p>
        </header>
        <main className="body">
          <div>
            <h2>Jugador</h2>
            <table border="1" style={{width: '100', textAlign: 'center' }}>
              <thead>
                <tr>
                  <th>Nombre</th>
                  <th>Skin</th>
                  <th>Salud</th>
                  <th>Ataque</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Steve</td>
                  <td><img src="/Componentes/Objetos/steve.png" alt="" /></td>
                  <td></td>
                  <td></td>
                </tr>
                <tr>
                  <td></td>
                  <td></td>
                  <td></td>
                  <td></td>
                </tr>
              </tbody>
            </table>
          </div>    
        </main>

        <footer className="footer">
          <p>Creado por X</p>
          <div className="icons">
            <a href=""></a>
            <a href=""></a>
            <a href=""></a>
          </div>
        </footer>
      </div>
    </>
  );
}

export default App;
