/*
    Title: Outland_Adventures_unit.sql
    Created by: Keith Olsen, Nathan Le, and Ivan Lopez-Kne
    Created on: 07/09/2023
    Description: Outland Adventure database initialization script.
*/

-- drop database if exists
DROP DATABASE IF EXISTS Outland_Adventure;

-- create Outland_Adventure database
CREATE DATABASE Outland_Adventure;

-- drop database user if exists 
DROP USER IF EXISTS 'adventure_user'@'localhost';


-- create adventure_user and grant them all privileges to the Outland_Adventure database 
CREATE USER 'adventure_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'adventure';

-- grant all privileges to the movies database to user adventure_user on localhost 
GRANT ALL PRIVILEGES ON Outland_Adventure.* TO 'adventure_user'@'localhost';
