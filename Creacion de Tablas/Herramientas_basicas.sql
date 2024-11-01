CREATE TABLE Herramientas_basicas(
  ID INT PRIMARY KEY AUTO_INCREMENT,
  Nombre_herramienta VARCHAR(50) NOT NULL,
  de_que_esta_hecho VARCHAR(50) NOT NULL,
  durabilidad INT NOT NULL,
  ataque DECIMAL NOT NULL,
  items_id INT,
  FOREIGN KEY (items_id) REFERENCES items(id)
)
