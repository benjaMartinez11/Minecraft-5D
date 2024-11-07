import React, { useState, useEffect } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";

function Articulo() {
  const { id } = useParams();
  const [articulo, setArticulo] = useState(null);

  useEffect(() => {
    axios
      .get(`http://localhost:5000/api/articulo/${id}`)
      .then((response) => {
        setArticulo(response.data);
      })
      .catch((error) => {
        console.error("Error al cargar el artículo:", error);
      });
  }, [id]);

  if (!articulo) {
    return <div>Cargando...</div>;
  }

  return (
    <div>
      <h2>{articulo.titulo}</h2>
      <p>{articulo.contenido}</p>
    </div>
  );
}

export default Articulo;
