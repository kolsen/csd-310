'''
Assignment: Module 8 - Movies Update and Delete 
Description: Connects to the movies db and updates and deletes fields
Created by: Keith Olsen
Created on: 07/01/2023
'''

import mysql.connector
from mysql.connector import errorcode

def show_films(cursor,title):
	# method to execute an inner join on all table,
    # iterate over the dataset and output the results to the terminal window

    try:
        # inner join query
        cursor.execute("SELECT film_name AS Name, film_director AS Director, genre_name AS Genre, studio_name AS 'Studio Name' FROM film INNER JOIN genre ON film.genre_id = genre.genre_id INNER JOIN studio ON film.studio_id = studio.studio_id")

        # get the results from the cursor object
        films = cursor.fetchall()
        print("\n -- {} -- ".format(title))

        # iterate through the film dataset and display the results
        for film in films:
            print("Film Name: {}\nDirector: {}\nGenre Name: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

    except mysql.connector.Error as error:
        print(f"Error querying database: {error}")

def get_studio_id(cursor, studioName):
    # Build the SQL query to retrieve the studio_id based on studio_name
    sql_select = "SELECT studio_id FROM studio WHERE studio_name = '" + studioName +"'"
    sql_insert = "INSERT INTO studio (studio_name) VALUES (%s)"
    values = (studioName,)
    
    # Execute the select query
    cursor.execute(sql_select)
    
    # Fetch the result
    result = cursor.fetchone()

    # If the studio doesn't exist, insert it and retrieve the new studio_id
    if result is None:
        cursor.execute(sql_insert,values)
        db.commit()
        # Execute the select query
        cursor.execute(sql_select)
         # Fetch the result
        result = cursor.fetchone()
    
    # Return the existing studio_id
    return result[0]

def get_genre_id(cursor, genreName):
    # Build the SQL query to retrieve the genre_id based on genre_name
    sql_select = "SELECT genre_id FROM genre WHERE genre_name = '" + genreName +"'"
    sql_insert = "INSERT INTO genre (genre_name) VALUES (%s)"
    values = (genreName,)

    # Execute the select query
    cursor.execute(sql_select)
    
    # Fetch the result
    result = cursor.fetchone()
    
    # If the genre doesn't exist, insert it and retrieve the new genre_id
    if result is None:
        cursor.execute(sql_insert,values)
        db.commit()
        # Execute the select query
        cursor.execute(sql_select)
         # Fetch the result
        result = cursor.fetchone()
    
    # Return the existing genre_id
    return result[0]

def insert_film(cursor, filmName, releaseDate, runtime, director, studioName, genreName):
    try:
        # Get the studio_id based on the studio_name
        studioId = str(get_studio_id(cursor, studioName))
        
        # Get the genre_id based on the genre_name
        genreId = str(get_genre_id(cursor, genreName))
        
        # Build the SQL query to insert a new record into the film table
        sql = "INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) " \
              "VALUES (%s, %s, %s, %s, %s, %s)"
        values = (filmName, releaseDate, runtime, director, studioId, genreId)

        # Execute the insert query
        cursor.execute(sql,values)

        # Commit the changes to the database
        db.commit()

    except mysql.connector.Error as error:
        print(f"Error inserting film: {error}")

def delete_film(cursor, filmName):
    try:
        # Build the SQL query to delete a film from the film table
        sql = "DELETE FROM film WHERE film_name = %s"
        
        # Execute the delete query
        cursor.execute(sql, (filmName,))

        # Commit the changes to the database
        db.commit()

    except mysql.connector.Error as error:
        print(f"Error deleting film: {error}")

def update_genre(cursor, filmTitle, genreName):
    # method to update film based on the title and genre name provided
    try:
        # Build the SQL query to find the film by film title and update the genre
        sql = "UPDATE film SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = %s) WHERE film_name = %s"

        # Execute the update query
        cursor.execute(sql, (genreName, filmTitle))

        # Commit the changes to the database
        db.commit()

    except mysql.connector.Error as error:
        print(f"Error updating genre: {error}")


# Connect to a database
config = {
"user": "movies_user",
"password": "popcorn",
"host": "127.0.0.1",
"database": "movies",
"raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  the supplied username or password are invalid")
        
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specific database does not exist")
    else:
        print (err)

cursor = db.cursor()
show_films(cursor,"Displaying Films")
insert_film(cursor,"The Shawshank Redemption","1994","142","Frank Darabont","Columbia Pictures","Drama")
show_films(cursor,"Displaying Films After Insert")
update_genre(cursor,"Alien","Horror")
show_films(cursor,"Displaying Films After Update - Changed Alien to Horror")
delete_film(cursor,"Gladiator")
show_films(cursor,"Displaying Films After Delete")
