CREATE TABLE Mob_hostil( 
  ID INT PRIMARY KEY AUTO_INCREMENT,
  nombre_hostil VARCHAR(50) NOT NULL,
  loot VARCHAR(50) NOT NULL,
  loot_exp BOOLEAN NOT NULL,
  movilidad VARCHAR(50) NOT NULL,
  ataque INT NOT NULL,
  vida DECIMAL,
  distancia_de_ataque VARCHAR(50) NOT NULL
)
