CREATE TABLE Bioma (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    nombre_bioma VARCHAR(255) NOT NULL,
    tipo_bioma ENUM('terrestre', 'acuático', 'subterráneo') NOT NULL,
    geografia ENUM('plano', 'montañoso', 'valle') NOT NULL, 
    temperatura DECIMAL(5,2) NOT NULL, 
    generar_mob_pass BOOLEAN,
    generar_mob_hoss BOOLEAN
);