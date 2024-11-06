CREATE TABLE Estructura (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    nombre_estructura VARCHAR(50) NOT NULL,
    biomas_ID INT,
    dimension_ID INT,
    FOREIGN KEY (biomas_ID) REFERENCES Bioma(ID),
    FOREIGN KEY (dimension_ID) REFERENCES Dimension(ID)
);