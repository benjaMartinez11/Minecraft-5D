INSERT INTO jefes (nombre_jefe, salud,daño_min, daño_max, ataque_distancia, ataque_mele
  , habilidad_especial, puede_ser_invocado, requisitos_invocacion, loot
) VALUES
(
    'Ender Dragon', 200, 3, 10, TRUE, TRUE, "Bola de fuego",
    'Cristales de Ender','Aliento de Dragón, Huevo de Dragón'
),
(
    'Wither', 450, 8, 68, TRUE, TRUE, "Cabeza de whiter",
    '3 cabezas de esqueleto Wither, 4 bloques de arena de almas',
    'Estrella de Nether'
),
(
    'Elder Guardian', 80, 3, 8, TRUE, FALSE, "Rayo laser",
    NULL,'Prismarina'
);