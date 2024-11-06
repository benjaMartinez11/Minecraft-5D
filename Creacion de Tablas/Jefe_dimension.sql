CREATE TABLE jefe_dimension (
    ID INT PRIMARY KEY,
    jefes_id INT,
    dimension_id INT,
    FOREIGN KEY (jefes_ID) REFERENCES Jefes(ID),
    FOREIGN KEY (dimension_ID) REFERENCES Dimension(ID)
);
