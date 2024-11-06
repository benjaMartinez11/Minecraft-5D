CREATE TABLE Herramientas (
    ID INT PRIMARY KEY,     
    nombre_herramienta VARCHAR(50), 
    como_se_hace VARCHAR(50),     
    crafteo VARBINARY(MAX),      
    cubos_ID INT,
    herramientas_basicas_ID INT,
    FOREIGN KEY (cubos_ID) REFERENCES Cubos(ID),  
    FOREIGN KEY (herramientas_basicas_ID) REFERENCES Herramientas_basicas(ID) 
);
