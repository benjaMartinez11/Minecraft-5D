CREATE TABLE Caracteristicas_jefe (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    nombre_ataque VARCHAR(50) NOT NULL,
    efecto VARCHAR(50) NOT NULL,  
    tipo_de_daño VARCHAR(50) NOT NULL,
    daño_a_distancia BOOLEAN,
    daño_mele BOOLEAN,
    daño_del_ataque DECIMAL,
    jefes_ID INT,
    FOREIGN KEY (jefes_ID) REFERENCES Jefe(ID)
);
