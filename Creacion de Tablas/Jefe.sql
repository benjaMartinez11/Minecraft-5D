CREATE TABLE jefes (
    jefe_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre_jefe VARCHAR(255) NOT NULL,
    salud_jefe INT,  
    puede_ser_invocado BOOLEAN,
    requisitos_invocacion VARCHAR(255),
    loot TEXT
);
