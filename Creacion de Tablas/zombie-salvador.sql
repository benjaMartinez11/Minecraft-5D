CREATE TABLE Zombie_salvador (
    ID INT PRIMARY KEY,
    items_ID INT,
    mob_id INT,
    FOREIGN KEY (items_ID) REFERENCES Item(ID),
    FOREIGN KEY (mob_id) REFERENCES Mobs(ID)
);
