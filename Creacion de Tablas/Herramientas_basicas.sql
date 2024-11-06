CREATE TABLE Herramientas_basicas(
  ID INT PRIMARY KEY AUTO_INCREMENT,
  nombre_herramienta VARCHAR(50) NOT NULL,
  de_que_esta_hecho VARCHAR(50) NOT NULL,
  durabilidad INT NOT NULL,
  ataque DECIMAL NOT NULL,
  items_ID INT,
  FOREIGN KEY (items_ID) REFERENCES items(ID)
)
