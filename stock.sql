-- Active: 1683026829664@@127.0.0.1@3306@stock

CREATE DATABASE stock;

USE stock;

CREATE TABLE
    admin(
        id INT PRIMARY KEY AUTO_INCREMENT,
        nom VARCHAR(20),
        password VARCHAR(20)
    );

CREATE TABLE
    produit(
        id INT PRIMARY KEY AUTO_INCREMENT,
        nom VARCHAR(20),
        prix DOUBLE(6, 3),
        qte_stock INT,
        seuil_alerte INT,
        date_derniere_entree DATE,
        date_derniere_sortie DATE,
        image_produit BLOB
    );

ALTER TABLE produit
ADD
    CONSTRAINT fk_admin FOREIGN KEY (id) REFERENCES admin(id);

ALTER TABLE admin ADD CONSTRAINT unique_admin UNIQUE (nom) 