CREATE TABLE mobs (
  mob_neutro_id INT,
  mob_pass_id INT,
  mob_hostil_id INT,
  mob_dimension_id INT,
  FOREIGN KEY (mob_neutro_id) REFERENCES mob_neutro(id)
  FOREIGN KEY (mob_pass_id) REFERENCES mob_pass(id)
  FOREIGN KEY (mob_hostil_id) REFERENCES mob_hostil(id)
  FOREIGN KEY (mob_dimesion_id) REFERENCES mob_dimesion(id)
);
