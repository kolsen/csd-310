'''
Assignment: Outland 
Description: Create Database and Tables for Outland Adventure
Created by: Keith Olsen, Nathan Le, and Ivan Lopez-Kne
Created on: 07/09/2023
'''

import mysql.connector
from mysql.connector import errorcode


try:
    # Configure connection to DB
    db = mysql.connector.connect(
        host = "127.0.0.1",
        database = "Outland_Adventure",
        user = "adventure_user",
        password = "adventure"

    )

    # Create cursor object to execute SQL queries
    cursor = db.cursor()

    # Drop Existing Tables
    cursor.execute("DROP TABLE IF EXISTS `Customer Order`;")
    cursor.execute("DROP TABLE IF EXISTS Equipment;")
    cursor.execute("DROP TABLE IF EXISTS Airfare;")
    cursor.execute("DROP TABLE IF EXISTS Trip;")
    cursor.execute("DROP TABLE IF EXISTS Location;")
    cursor.execute("DROP TABLE IF EXISTS `Visa Requirements`;")
    cursor.execute("DROP TABLE IF EXISTS Inoculation;")
    cursor.execute("DROP TABLE IF EXISTS Employee;")
    cursor.execute("DROP TABLE IF EXISTS Customers;")
    cursor.execute("DROP TABLE IF EXISTS Department;")

    # Create the Outland Adventures tables

    cursor.execute("""
                   CREATE TABLE Department (
                    department_ID INT NOT NULL AUTO_INCREMENT,
                    department_name VARCHAR(30),
                    department_description VARCHAR(50),
                    department_email VARCHAR(50),
                    department_phone VARCHAR(20),
                    PRIMARY KEY(department_ID)
                   );
                   """)
    
       
    cursor.execute("""
               CREATE TABLE Customers (
                   customer_ID INT NOT NULL AUTO_INCREMENT,
                    customer_name VARCHAR(20) NOT NULL,
                    customer_phone VARCHAR(20),
                    customer_email VARCHAR(50),
                    customer_address VARCHAR(50),
                    customer_preferences VARCHAR(30),
                    customer_requirements VARCHAR(30),
                    PRIMARY KEY(customer_ID)

               );
               """)
    
    cursor.execute("""
                   CREATE TABLE Employee (
                    employee_ID INT NOT NULL AUTO_INCREMENT,
                    employee_name VARCHAR(50) NOT NULL,
                    department_ID INT,
                    employee_role VARCHAR(50),
                    PRIMARY KEY(employee_ID),
                    CONSTRAINT fk_department
                    FOREIGN KEY (department_ID) REFERENCES Department(department_ID)
                   );
                   """)
    
        
    cursor.execute("""
                   CREATE TABLE Inoculation (
                   vaccine_ID INT NOT NULL AUTO_INCREMENT,
                   vaccine_name VARCHAR(30),
                   recomended_dasage VARCHAR(15),
                   medical_information VARCHAR(100),
                   PRIMARY KEY(vaccine_ID)
                   );
                   """)
    
    cursor.execute("""
                   CREATE TABLE `Visa Requirements` (
                   visa_type VARCHAR(100),
                   application_process VARCHAR(200),
                   visa_fees VARCHAR(10),
                   PRIMARY KEY (visa_type)
                   );
                   """)
    
        
    cursor.execute("""
               CREATE TABLE Location (
                location_ID INT NOT NULL AUTO_INCREMENT,
                location_name VARCHAR(30),
                location_details VARCHAR(50),
                vaccine_ID INT,
                visa_type VARCHAR(100),
                PRIMARY KEY (location_ID),
                CONSTRAINT fk_vaccine
                FOREIGN KEY (vaccine_ID) REFERENCES Inoculation(vaccine_ID),
                CONSTRAINT fk_visa_type
                FOREIGN KEY (visa_type) REFERENCES `Visa Requirements`(visa_type)
               );
               """)
    
    cursor.execute("""
                   CREATE TABLE Trip (
                    trip_ID INT NOT NULL AUTO_INCREMENT,
                    customer_ID INT,
                    vaccine_ID INT,
                    location_ID INT,
                    PRIMARY KEY(trip_ID),
                    CONSTRAINT fk_customer
                    FOREIGN KEY (customer_ID) REFERENCES Customers(customer_ID),
                   CONSTRAINT fk_inoculation
                    FOREIGN KEY (vaccine_ID) REFERENCES Inoculation(vaccine_ID),
                   CONSTRAINT fk_tripLocation
                    FOREIGN KEY (location_ID) REFERENCES Location(location_ID)
                   );
                   """)
    
    cursor.execute("""
                   CREATE TABLE Airfare (
                    flight_number VARCHAR(20) NOT NULL,
                    arrival_date DATE,
                    departure_date DATE,
                    airfare_cost DECIMAL(10, 2),
                    location_ID INT,
                    trip_ID INT,
                    PRIMARY KEY(flight_number),
                   CONSTRAINT fk_airfareLocation
                    FOREIGN KEY (location_ID) REFERENCES Location(location_ID),
                   CONSTRAINT fk_trip
                    FOREIGN KEY (trip_ID) REFERENCES Trip(trip_ID)
                   );
                   """)
    
    cursor.execute("""
                CREATE TABLE Equipment (
                equipment_ID INT NOT NULL AUTO_INCREMENT,
                equipment_name VARCHAR(50),
                equipment_type VARCHAR(50),
                customer_ID INT,
                PRIMARY KEY (equipment_ID),
                   CONSTRAINT fk_equipCustomer
                FOREIGN KEY (customer_ID) REFERENCES Customers(customer_ID)
                );
                """)

    cursor.execute("""
                   CREATE TABLE `Customer Order` (
                   order_ID INT NOT NULL AUTO_INCREMENT,
                   equipment_ID VARCHAR(30),
                   equipment_quantity VARCHAR(15),
                   order_status VARCHAR(100),
                   customer_ID INT,
                   employee_ID INT,
                   PRIMARY KEY(order_ID),
                   CONSTRAINT fk_orderCustomer
                   FOREIGN KEY (customer_ID) REFERENCES Customers(customer_ID),
                   CONSTRAINT fk_orderEmployee
                   FOREIGN KEY (employee_ID) REFERENCES Employee(employee_ID)
                   );
                   """)
    
    
except mysql.connector.Error as err:
    print(err)

finally:
	db.close()
	