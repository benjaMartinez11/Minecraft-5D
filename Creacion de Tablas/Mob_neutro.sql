CREATE TABLE Mob_neutro( 
  ID INT PRIMARY KEY AUTO_INCREMENT,
  nombre_neutro VARCHAR(50) NOT NULL,
  loot VARCHAR(50) NOT NULL,
  loot_exp BOOLEAN NOT NULL,
  reproduccion BOOLEAN NOT NULL,
  movilidad VARCHAR(50) NOT NULL,
  vida DECIMAL,
  ataque INT NOT NULL
);
