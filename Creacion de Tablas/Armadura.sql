CREATE TABLE Armadura(
  ID INT PRIMARY KEY AUTO_INCREMENT,
  nombre_armadura VARCHAR(50) NOT NULL,
  de_que_esta_hecho VARCHAR(50) NOT NULL,
  durabilidad INT NOT NULL,
  defensa INT NOT NULL,
  durabilidad_Unidad VARCHAR (50),
  items_id INT,
  items_ID INT,
  FOREIGN KEY (items_ID) REFERENCES items(ID)
);