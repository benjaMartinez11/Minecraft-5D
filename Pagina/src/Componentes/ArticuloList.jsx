import React, { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

function ArticuloList() {
  const [articulos, setArticulos] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:5000/api/articulos")
      .then((response) => {
        setArticulos(response.data);
      })
      .catch((error) => {
        console.error("Error al cargar los artículos:", error);
      });
  }, []);

  return (
    <div>
      <h2>Artículos</h2>
      <ul>
        {articulos.map((articulo) => (
          <li key={articulo.id}>
            <Link to={`/articulo/${articulo.id}`}>{articulo.titulo}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ArticuloList;
