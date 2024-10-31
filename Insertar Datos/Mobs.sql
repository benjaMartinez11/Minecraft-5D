INSERT INTO mobs(nombre_mob, tipo_mob, daño_mob, movilidad, animal, mounstro, humano, distancia_ataque, interaccion_id, reproduccion, vida_mob);
VALUES ('Zombi', 'Hostil', 3, 'Terrestre', False, True, False, 'Cuerpo a cuerpo', 'Golpear', False, 20),
('Esqueleto', 'Hostil', 3, 'Terrestre', False, True, False, 'A distancia', 'Golpear', False, 20),
('Creeper', 'Hostil', 42, 'Terrestre', False, True, False, 'Cuerpo a cuerpo', 'Golpear', False, 20),
('Araña', 'Neutral', 2, 'Terrestre', False, True, False, 'Cuerpo a cuerpo', 'Golpear', False, 16),
('Enderman', 'Neutral', 6, 'Terrestre', False, True, False, 'Cuerpo a cuerpo', 'Golpear', False, 40),
('Cerdo', 'Pasivo', 0, 'Terrestre', True, False, False, Null, 'Golpear, Alimentar o Montar', True, 10),
('Oveja', 'Pasivo', 0, 'Terrestre', True, False, False, Null, 'Golpear, Alimentar o Trasquilar', True, 8),
('Vaca', 'Pasivo', 0, 'Terrestre', True, False, False, Null, 'Golpear, Alimentar o Ordeñar', True, 10),
('Pollo', 'Pasivo', 0, 'Terrestre', True, False, False, Null, 'Golpear o Alimentar', True, 4),
('Caballo', 'Pasivo', 0, 'Terrestre', True, False, False, Null, 'Golpear, Alimentar o Montar', True, 24),
('Ghast', 'Hostil', 12, 'Volador', False, True, False, 'A distancia', 'Golpear', False, 10); 