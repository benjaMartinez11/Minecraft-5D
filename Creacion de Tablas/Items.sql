CREATE TABLE Item (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    herramientas_ID INT,
    armadura_ID INT,
    agricultura_ID INT,
    comida_ID INT,
    encantamientos_ID INT,
    herramientas_basicas_ID INT,
    cubos_ID INT,
    FOREIGN KEY (cubos_ID) REFERENCES Cubos(ID),
    FOREIGN KEY (herramientas_ID) REFERENCES Herramientas(ID),
    FOREIGN KEY (herramientas_basicas_ID) REFERENCES Herramientas_basicas(ID),
    FOREIGN KEY (armadura_ID) REFERENCES Armadura(ID),
    FOREIGN KEY (agricultura_ID) REFERENCES Agricultura(ID),
    FOREIGN KEY (comida_ID) REFERENCES Comida(ID),
    FOREIGN KEY (encantamientos_ID) REFERENCES Encantamientos(ID)
);
