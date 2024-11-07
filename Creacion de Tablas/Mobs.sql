CREATE TABLE Mobs (
  ID INT PRIMARY KEY AUTO_INCREMENT,
  mob_neutro_ID INT,
  mob_pass_ID INT,
  mob_hostil_ID INT,
  dimension_ID INT,
  FOREIGN KEY (mob_neutro_ID) REFERENCES Mob_neutro(ID),
  FOREIGN KEY (mob_pass_ID) REFERENCES Mob_pass(ID),
  FOREIGN KEY (mob_hostil_ID) REFERENCES Mob_hostil(ID),
  FOREIGN KEY (dimension_ID) REFERENCES Dimension(ID)
);
