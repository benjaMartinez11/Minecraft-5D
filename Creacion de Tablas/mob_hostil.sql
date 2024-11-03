CREATE TABLE mob_neutro( 
  ID INT PRIMARY KEY AUTO_INCREMENT,
  Nombre_hostil VARCHAR(50) NOT NULL,
  loot VARCHAR(50) NOT NULL,
  loot_exp BOOLEAN NOT NULL,
  ataque INT NOT NULL,
  vida DECIMAL,
  movilidad VARCHAR(50) NOT NULL,
  disctancia_de_ataque VARCHAR(50) NOT NULL
)
