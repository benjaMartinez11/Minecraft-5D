CREATE TABLE items (
    item_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre_item VARCHAR(255) NOT NULL,
    tipo_item ENUM('herramienta', 'bloque', 'alimento', 'material', 'poción', 'decoración', 'arma') NOT NULL,
    subcategoria_item VARCHAR(100),
    durabilidad INT DEFAULT 0,
    apilable BOOLEAN,
    descripcion TEXT,
    interaccion BOOLEAN,
    se_puede_craftear BOOLEAN
);
