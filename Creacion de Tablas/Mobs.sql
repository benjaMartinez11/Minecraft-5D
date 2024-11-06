CREATE TABLE mobs (
  ID INT PRIMARY KEY AUTO_INCREMENT,
  mob_neutro_ID INT,
  mob_pass_ID INT,
  mob_hostil_ID INT,
  dimension_ID INT,
  FOREIGN KEY (mob_neutro_ID) REFERENCES Mob_neutro(id)
  FOREIGN KEY (mob_pass_ID) REFERENCES Mob_pass(id)
  FOREIGN KEY (mob_hostil_ID) REFERENCES Mob_hostil(id)
  FOREIGN KEY (dimension_ID) REFERENCES Dimension(id)
);
