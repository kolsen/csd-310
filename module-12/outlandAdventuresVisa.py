'''
Description: Connects to the Outland_Adventure db and runs report on visa requirements.
Created by: Keith Olsen, Nathan Le, Ivan Lopez-Kne
Created on: 07/14/2023
Updated By: Keith Olsen 07/22/2023
Update: Updated report to be more readable
'''

import mysql.connector
from mysql.connector import errorcode

# Configure connection to DB
db_config = {
    "host": "127.0.0.1",
    "user": "adventure_user",
    "password": "adventure",
    "database": "Outland_Adventure",
}


def execute_query(query):
    connection = mysql.connector.connect(**db_config)
    # Create cursor object to execute SQL queries
    cursor = connection.cursor()

    # Connect to Database
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

def display_report(rows):
    
    print("--- VISA REQUIREMENTS ---")
    
    print("{:<28} | {:<12} | {:<10}| {:<14}| {:<10}".format("Visa Type","Visa Process","Visa Fees","Location Name","Location Details"))
    print("-" * 90)

    for row in rows:
        visa_type, application_process, visa_fees, location_name, location_details = row
        print(f"{visa_type:28} | {application_process:12} | {visa_fees:9} | {location_name:13} | {location_details}")

if __name__ == "__main__":
    query = """
    SELECT v.visa_type, v.application_process, v.visa_fees, l.location_name, l.location_details
    FROM location l
    JOIN `visa requirements` v ON l.visa_type = v.visa_type
    """

    result_rows = execute_query(query)

    if result_rows:
        display_report(result_rows)
    else:
        print("No data found.")