CREATE TABLE Jugador (
    jugador_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre_usuario VARCHAR(50) NOT NULL,
    ataque DECIMAL,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP, 
    salud FLOAT DEFAULT 20,  
    armadura_ID INT,
    FOREIGN KEY (armadura_ID) REFERENCES Armadura(ID)
);