import React, { useState } from "react";
import "./index.css";
import Header from "./Componentes/Header";
import Navbar from "./Componentes/Navbar";
import Footer from "./Componentes/Footer";

function App() {

  //const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <header className="header">
          <p>Minecraft</p>
        </header>
        <main className="body">
          <div>
            <h2>Items</h2>
            <table border="1" style={{width: '100', textAlign: 'center' }}>
              <thead>
                <tr>
                  <th></th>
                  <th></th>
                  <th></th>
                  <th></th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td></td>
                  <td></td>
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
