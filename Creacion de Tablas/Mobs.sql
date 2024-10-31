CREATE TABLE mobs (
    mob_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre_mob VARCHAR(255) NOT NULL,
    tipo_mob ENUM('hostil', 'neutral', 'pasivo') NOT NULL,
    salud_mob INT DEFAULT 10,
    daño_mob INT DEFAULT 0,  
    ataque_a_distancia BOOLEAN,
    habilidad_especial VARCHAR(100),
    reproduccion BOOLEAN,
    luminosidad_minima INT DEFAULT 0,
    generacion_natural BOOLEAN, 
    nace_de VARCHAR(100),
    invocacion_requerida VARCHAR(100)
);