CREATE TABLE dimensiones (
    dimension_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre_dimension ENUM('Overworld', 'Nether', 'End') NOT NULL,
    descripcion_dimension TEXT,
    puede_generar_mobs BOOLEAN,
);