CREATE TABLE Mob_dimension (
    ID INT PRIMARY KEY,
    mob_id INT,
    dimension_id INT,
    FOREIGN KEY (mob_id) REFERENCES mob(ID),
    FOREIGN KEY (dimension_id) REFERENCES dimension(ID)
);
