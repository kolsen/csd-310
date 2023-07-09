
INSERT INTO Department(department_name, department_description, department_email, department_phone)
Values
	('Sales','Handles sales','sales@outlandadventures.com','555-867-5309'),
	('Operations','Manages trips','operations@@outlandadventures.com','555-555-5555'),
	('Marketing','Handles Marketing','marketing@outlandadventures.com','444-444-4444'),
	('Administration','Handles Administration duties and runs business','admin@outlandadventures.com','333-333-3333'),
	('Supplies','Handles Equipment','supplies@outlandadventures.com','111-111-1111'),
	('Tour Guides','provides guided tours','guides@outlandadventures.com','101-101-1010');

INSERT INTO customers(customer_name, customer_phone, customer_email, customer_address, customer_preferences, customer_requirements)
VALUES('Hiba Dotson', '202 918 2132','sharo362@btcprestige.net', '197 Hickory Lane', '',''),
        ('Cameron Tanner', '814 836 4881','ssmirnowa@lvufaa.xyz', '4228 Pike Street', 'Hate bugs',''),
        ('Hayden Oconnor', '240 328 8424','chernikovshura@joeneo.com', '4921 Conifer Drive', '',''),
        ('Haris Blaese', '252 744 6585','o0honeybee0o@tlwpleasure.com', '236 Richland Avenue', 'gets seasick',''),
        ('Calum Snow', '505 644 1779','dinosaurdanceparty@weinzed.org', '119 Waterview Lane', '',''),
        ('Lina Neil', '614 797 2806','r1skytr0uble@airportlimoneworleans.com', '3856 Clarence Court', '','');


INSERT INTO Employee(employee_name, department_ID, employee_role)
VALUES('John Smith', 1, 'Sales Representative'),
		('John "Mac" MacNell', 6, 'Tour Guide'),
		('Dimitrios Stravopolous', 4, 'Supplies Manager'),
		('Sophia Davis', 2, 'Trip Coordinator'),
		('D.B. "Duke" Marland', 6, 'Tour Guide'),
		('Anita Gallegos', 3, 'Marketing Assistant'),
		('Blythe Timmerson', 4, 'CEO'),
		('Jim Ford', 4, 'COO');

INSERT INTO Inoculation(vaccine_name, recomended_dasage, medical_information)
VALUES ('Herpes',2,'keep cold'),
        ('Rabies',1,'keep cold'),
        ('Polio',1,'keep cold'),
        ('Tetanus',2,'keep cold'),
        ('Varicella',1,'keep cold'),
        ('Rotavirus',1,'keep cold');


INSERT INTO `visa requirements`(visa_type, application_process, visa_fees)
VALUES ('UK Visa','Online','$250'),
        ('KAZA univisa','Online','$280'),
        ('Central American Single Visa','Online','$310'),
        ('Schengen Visa','Online','$225'),
        ('Canada Visa','Online','$325'),
        ('East African Tourist Visa','Online','$300');


INSERT INTO Location(location_name, location_details, vaccine_ID, visa_type)
VALUES('Great Britain','Big Ben','2','UK Visa'),
        ('Botswana','sand','5','KAZA univisa'),
        ('Canada','lakes','2','Central American Single Visa'),
        ('Romania','Bran Castle','6','Schengen Visa'),
        ('zambia','African Animals','4','Canada Visa'),
        ('Belize','Mayan Ruins','4','East African Tourist Visa');



INSERT INTO trip(customer_ID, vaccine_ID, location_ID)
VALUES (6,2,1),
		(5,5,2),
		(4,2,1),
		(1,2,3),
		(2,4,5),
		(3,6,4);



INSERT INTO Airfare(flight_number, arrival_date, departure_date, airfare_cost, location_ID, trip_ID)
VALUES('AA123','2023-06-12','2023-07-04',732.50,1, 1),
    ('DL456','2023-09-02','2023-10-15',1057.80, 2, 2),
    ('UA789','2023-12-08','2024-01-21',876.95,3, 3),
    ('BA234','2024-03-05','2024-04-18',639.20,4, 4),
    ('LH567','2024-05-23','2024-07-06',1203.75,5, 5),
    ('EK890','2024-08-17','2024-09-29',989.60,6, 6);

INSERT INTO equipment(equipment_name, equipment_type, customer_id)
VALUES('Backpack','Hiking Gear', 1),
    ('Tent','Camping Gear', 2),
    ('Raft','Water Gear', 3),
    ('Trekking Pole','Hiking Gear', 4),
    ('Water Shoes','Water Gear', 5), 
    ('Bike','Transport', 6);



INSERT INTO `Customer Order`(equipment_ID, equipment_quantity, order_status, customer_ID, employee_ID)
Values(1, '2','Processing', 1, 1),
    (2, '3','Fulfilled', 2, 2),
    (3, '1','Fulfilled', 3, 3),
    (4, '5','Processing',4, 4),
    (5, '2','Processing',5, 5),
    (6, '2','Processing',6, 6);