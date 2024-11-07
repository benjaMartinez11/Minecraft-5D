CREATE TABLE Mob_dimension (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    mob_id INT,
    dimension_id INT,
    FOREIGN KEY (mob_id) REFERENCES Mobs(ID),
    FOREIGN KEY (dimension_id) REFERENCES Dimension(ID)
);
