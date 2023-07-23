'''
Description: Connects to the Outland_Adventure db and runs report on equipment rentals.
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
    # Display Report title
    print("--- Equipment Currently Rented Report ---")
    # Display Header
    print("{:<12} | {:<18} | {:<15} | {:<15} | {:<14} | {:<40}| {:<10}".format("Equipment ID","Equipment Assigned","Equipment Type","Customer","Customer Phone","Customer Email","Location"))
    print("-" * 150)

    for row in rows:
        equipment_id, equipment_assigned, equipment_type, customer, customer_phone, customer_email, location = row
        print(f"{equipment_id:12} | {equipment_assigned:18} | {equipment_type:15} | {customer:15} | {customer_phone:14} | {customer_email:40} | {location}")

if __name__ == "__main__":
    query = """
    SELECT e.equipment_ID, e.equipment_name AS Equipment_Assigned, e.equipment_type, c.customer_name AS Customer, c.customer_phone, c.customer_email, l.location_name AS Location
    FROM equipment e
    JOIN customers c ON e.customer_ID = c.customer_ID
    JOIN trip t ON e.customer_ID = t.customer_ID
    JOIN location l ON t.location_ID = l.location_ID
    WHERE e.customer_ID IS NOT NULL;
    """

    result_rows = execute_query(query)

    if result_rows:
        display_report(result_rows)
    else:
        print("No data found.")
