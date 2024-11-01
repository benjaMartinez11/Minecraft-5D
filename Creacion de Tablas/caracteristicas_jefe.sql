CREATE TABLE caracteristicas_jefe (
    caracteristicas_jefe_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre_ataque VARCHAR(50) NOT NULL,
    efecto VARCHAR(50) NOT NULL,  
    tipo_de_daño VARCHAR(50) NOT NULL,
    daño_a_distancia BOOLEAN,
    daño_mele BOOLEAN,
    daño_del_ataque DECIMAL,
    Jefe_id INT, --Esto es para indentificar de quien es el ataque
    FOREIGN KEY (Jefe_id) REFERENCES Jefe(id);
);
