CREATE TABLE Item (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    nombre_item VARCHAR(255) NOT NULL,
    herramientas_ID INT,
    armadura_ID INT,
    agricultura_ID INT,
    comida_ID INT,
    encantamientos_ID INT,
    FOREIGN KEY (herramientas_ID) REFERENCES Herramientas(ID),
    FOREIGN KEY (armadura_ID) REFERENCES Armadura(ID),
    FOREIGN KEY (agricultura_ID) REFERENCES Agricultura(ID),
    FOREIGN KEY (comida_ID) REFERENCES Comida(ID),
    FOREIGN KEY (encantamientos_ID) REFERENCES Encantamientos(ID)
);
