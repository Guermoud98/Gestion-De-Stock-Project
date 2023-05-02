CREATE DATABASE stock;
SHOW DATABASES;
USE stock;
CREATE TABLE utilisateur(
id INT PRIMARY KEY AUTO_INCREMENT, 
nom VARCHAR(20), 
password VARCHAR(20)
); 
CREATE TABLE produit(
id INT PRIMARY KEY AUTO_INCREMENT,
nom VARCHAR(20),
prix DOUBLE(6,3),
qte_stock INT,
seuil_alerte INT,
date_derniere_entree DATE ,
date_derniere_sortie DATE,
image_produit BLOB
);
INSERT INTO utilisateur(nom, password) VALUES ("maria", "hellohellutilisateuro12");
INSERT INTO utilisateur(nom, password) VALUES ("neha", "2003neha");
SELECT * FROM utilisateur;
