// server.js
const express = require("express");
const mysql = require("mysql"); // Asumiendo que tu base de datos es MySQL
const cors = require("cors");

const app = express();
app.use(cors()); // Permite que React acceda al servidor

const db = mysql.createConnection({
  host: "10.9.120.5",
  port: 8080,
  user: "minecraft",
  password: "minecraft111",
  database: "minecraft  ",
});

app.get("/datos", (req, res) => {
  db.query("SELECT * FROM tabla", (error, results) => {
    if (error) {
      return res.status(500).json({ error: "Error en la consulta" });
    }
    res.json(results);
  });
});

const PORT = 5000;
app.listen(PORT, () => {
  console.log(`Servidor ejecutándose en http://localhost:${PORT}`);
});
