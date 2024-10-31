import { useState } from "react";
import "./App.css";
import { FaGithub } from "react-icons/fa";
import { FaYoutube } from "react-icons/fa";
import { FaInstagramSquare } from "react-icons/fa";

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
            <table border="1" style={{ width: "100%", textAlign: "center" }}>
              <thead></thead>
              <tbody>
                <tr>
                  <td>
                    <img src="/objetos/tiirr.png" alt="" className="imagen" />
                  </td>
                  <td>
                    <img src="/objetos/espada.png" alt="" className="imagen" />
                  </td>
                  <td>
                    <img src="/objetos/manzana.png" alt="" className="imagen" />
                  </td>
                  <td>
                    <img src="/objetos/hierro.png" alt="" className="imagen" />
                  </td>
                </tr>
                <tr>
                  <td>
                    <img src="/objetos/objet.png" alt="" className="imagen" />
                  </td>
                  <td>
                    <img src="/objetos/objet.png" alt="" className="imagen" />
                  </td>
                  <td>
                    <img src="/objetos/objet.png" alt="" className="imagen" />
                  </td>
                  <td>
                    <img src="/objetos/objet.png" alt="" className="imagen" />
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
          <div>
            <h2>Dimensiones</h2>
            <table border="1" style={{ width: "100%", textAlign: "center" }}>
              <thead></thead>
              <tbody>
                <tr>
                  <td>
                    <img src="/objetos/tiirr.png" alt="" className="imagen" />
                  </td>
                  <td>
                    <img src="/objetos/espada.png" alt="" className="imagen" />
                  </td>
                  <td>
                    <img src="/objetos/manzana.png" alt="" className="imagen" />
                  </td>
                  <td>
                    <img src="/objetos/hierro.png" alt="" className="imagen" />
                  </td>
                </tr>
                <tr>
                  <td>
                    <img src="/objetos/objet.png" alt="" className="imagen" />
                  </td>
                  <td>
                    <img src="/objetos/objet.png" alt="" className="imagen" />
                  </td>
                  <td>
                    <img src="/objetos/objet.png" alt="" className="imagen" />
                  </td>
                  <td>
                    <img src="/objetos/objet.png" alt="" className="imagen" />
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </main>

        <footer className="footer">
          <p>creado x medio curso</p>
          <div className="icons">
            <a href="https://www.youtube.com/">
              <FaYoutube size={30} />
            </a>
            <a href="https://github.com/">
              <FaGithub size={30} />
            </a>
            <a href="https://www.instagram.com/">
              <FaInstagramSquare size={30} />
            </a>
          </div>
        </footer>
      </div>
    </>
  );
}

export default App;
