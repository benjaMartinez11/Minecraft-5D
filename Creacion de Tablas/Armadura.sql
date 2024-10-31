CREATE TABLE Armadura(
  ID INT PRIMARY KEY AUTO_INCREMENT,
  Nombre_armadura VARCHAR(50) NOT NULL,
  de_que_esta_hecho VARCHAR(50) NOT NULL,
  durabilidad INT NOT NULL,
  defensa INT NOT NULL,
  Durabilidad_Unidad VARCHAR (50),
  items_id INT,
  FOREIGN KEY (items_id) REFERENCES items(id)
)