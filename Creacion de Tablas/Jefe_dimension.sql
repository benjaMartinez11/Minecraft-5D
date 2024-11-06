CREATE TABLE jefe_dimension (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    jefes_ID INT,
    dimension_ID INT,
    FOREIGN KEY (jefes_ID) REFERENCES Jefes(ID),
    FOREIGN KEY (dimension_ID) REFERENCES Dimension(ID)
);
