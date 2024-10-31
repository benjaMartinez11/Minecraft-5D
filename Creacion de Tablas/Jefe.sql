CREATE TABLE jefes (
    jefe_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre_jefe VARCHAR(255) NOT NULL,
    salud_jefe INT, 
    dañomax_jefe INT , 
    dañomin_jefe INT,
    ataque_a_distancia BOOLEAN,  
    habilidad_especial VARCHAR(100),  
    puede_ser_invocado BOOLEAN,
    requisitos_invocacion VARCHAR(255),
    biomas_donde VARCHAR(100),
    dimension_donde VARCHAR(100),
    loot TEXT
);