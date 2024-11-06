CREATE TABLE Mob_dimension (
    ID INT PRIMARY KEY,
    mob_id INT,
    dimension_id INT,
    FOREIGN KEY (mob_id) REFERENCES Mob(ID),
    FOREIGN KEY (dimension_id) REFERENCES Dimension(ID)
);
