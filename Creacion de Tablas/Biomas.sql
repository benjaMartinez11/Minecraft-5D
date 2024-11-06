CREATE TABLE biomas (
    bioma_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre_bioma VARCHAR(255) NOT NULL,
    generar_mob_pass BOOLEAN,
    generar_mob_hoss BOOLEAN,
    descripcion text
);