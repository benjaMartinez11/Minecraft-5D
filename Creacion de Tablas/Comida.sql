CREATE TABLE Comida(
  ID INT PRIMARY KEY AUTO_INCREMENT,
  Nombre_comida VARCHAR(50) NOT NULL,
  efecto VARCHAR(50) NOT NULL,
  recuperar_muslos DECIMAL NOT NULL,
  saturacion_de_recuperacion DECIMAL NOT NULL,
  como_se_consigue TEXT,
  reseta VARCHAR(50) NOT NULL,
  items_id,
  FOREIGN KEY (items_id) REFERENCES items(id)
)