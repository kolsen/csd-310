'''
Assignment: Module 7 - Movies Query 
Description: Connects to the movies db and and runs queries for studio, genre, film and director records
Created by: Keith Olsen
Created on: 07/01/2023
'''

import mysql.connector
from mysql.connector import errorcode

config = {
	"user": "movies_user",
	"password": "popcorn",
	"host": "127.0.0.1",
	"database": "movies",
	"raise_on_warnings": True
}

try:
	db = mysql.connector.connect(**config)
	
	print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"],config["host"],config["database"]))
	
	#Query Studio records
	cursor = db.cursor()
	cursor.execute("SELECT * FROM studio")
	studios = cursor.fetchall()
	print("-- DISPLAYING Studio RECORDS --")
	for studio in studios:
		print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))
    
	#Query Genre records
	cursor.execute("SELECT * FROM genre")
	genres = cursor.fetchall()
	print("-- DISPLAYING Genre RECORDS --")
	for genre in genres:
		print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

	#Query Film records
	cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
	films = cursor.fetchall()
	print("-- DISPLAYING Film RECORDS --")
	for film in films:
		print("Film Name: {}\nFilm Runtime: {}\n".format(film[0], film[1]))
	
	#Query for Director from Film table
	cursor.execute("Select film_name, film_director FROM film ORDER By film_releaseDate DESC")
	films = cursor.fetchall()
	print("-- DISPLAYING Director RECORDS in Order --")
	for film in films:
		print("Film Name: {}\nDirector: {}\n".format(film[0], film[1]))
	
except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("  the supplied username or password are invalid")
		
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("  The specific database does not exist")
	else:
		print (err)
	
finally:
	db.close()
	