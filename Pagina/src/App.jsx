import React, { useState, useEffect } from "react";
import Header from "./Componentes/Header";
import Body from "./Componentes/Body";
import Footer from "./Componentes/footer";
import { FaInstagram } from "react-icons/fa";
import { FaGithub } from "react-icons/fa";
import { FaWhatsapp } from "react-icons/fa";
import "./index.css";

const App = () => {
  const [view, setView] = useState("inicio");
  const [jugador, setJugador] = useState([]);
  const [herramientas_basicas, setHerramientas] = useState([]);
  const [armadura, setArmadura] = useState([]);
  const [comida, setComida] = useState([]);
  const [mob_pass, setMob_pass] = useState([]);
  const [mob_neutro, setMob_neutro] = useState([]);
  const [mob_hostil, setmob_hostil] = useState([]);
  const [jefes, setJefes] = useState([]);
  const [caracteristicas_jefe, setCaracteristicas_jefe] = useState([]);
  const [bioma, setBioma] = useState([]);
  const [estructura, setEstructura] = useState([]);
  const [dimension, setDimension] = useState([]);
  const [agricultura, setAgricultura] = useState([]);
  const [cubos, setCubos] = useState([]);

  // Fetching de todos los datos
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
    fetch("http://127.0.0.1:5000/comida")
      .then((data) => data.json())
      .then((response) => setComida(response));
    fetch("http://127.0.0.1:5000/mob_pass")
      .then((data) => data.json())
      .then((response) => setMob_pass(response));
    fetch("http://127.0.0.1:5000/mob_neutro")
      .then((data) => data.json())
      .then((response) => setMob_neutro(response));
    fetch("http://127.0.0.1:5000/mob_hostil")
      .then((data) => data.json())
      .then((response) => setmob_hostil(response));
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
      <Header setView={setView} />
      <Body
        view={view}
        renderTable={renderTable}
        jugador={jugador}
        herramientas_basicas={herramientas_basicas}
        armadura={armadura}
        comida={comida}
        mob_pass={mob_pass}
        mob_neutro={mob_neutro}
        mob_hostil={mob_hostil}
        jefes={jefes}
        caracteristicas_jefe={caracteristicas_jefe}
        bioma={bioma}
        estructura={estructura}
        dimension={dimension}
        agricultura={agricultura}
        cubos={cubos}
      />
      <Footer />
    </>
  );
};


export default App;
