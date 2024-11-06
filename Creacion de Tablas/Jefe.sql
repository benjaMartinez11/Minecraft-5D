CREATE TABLE Jefes (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    nombre_jefe VARCHAR(50) NOT NULL,
    salud INT,  
    movilidad VARCHAR(50) NOT NULL,
    puede_ser_invocado BOOLEAN,
    requisitos_invocacion VARCHAR(255),
    loot TEXT,
    loot_exp, BOOLEAN,
    jefe_info_ID INT,
    FOREIGN KEY (jefe_info_ID) REFERENCES Caracteristicas_jefe(ID),
    );
