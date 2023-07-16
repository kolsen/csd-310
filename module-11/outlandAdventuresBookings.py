'''
Description: Connects to the Outland_Adventure db and runs report on Current Bookings.
Created by: Keith Olsen, Nathan Le, Ivan Lopez-Kne
Created on: 07/14/2023
'''


import mysql.connector

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
    print("--- Current bookings for Outland Adventures ---")
    #Display Header
    print("Trip ID | Customer ID | Vaccine Needed | Location Name | Flight Number | Arrival Date | Departure Date | Airfare Cost")
    print("-" * 110)

    for row in rows:
        trip_id, customer_id, vaccine_name, location_name, flight_number, arrival_date, departure_date, airfare_cost = row
        print(f"{trip_id:7} | {customer_id:11} | {vaccine_name:9} | {location_name:13} | {flight_number:13} | {arrival_date} | {departure_date} | {airfare_cost}")

if __name__ == "__main__":
    query = """
    SELECT t.trip_ID, t.customer_ID, i.vaccine_name, l.location_name, a.flight_number, a.arrival_date, a.departure_date, a.airfare_cost
    FROM trip t
    JOIN location l ON t.location_ID = l.location_ID
    JOIN airfare a ON t.trip_ID = a.trip_ID
    JOIN inoculation i ON t.vaccine_ID = i.vaccine_ID
    WHERE t.customer_ID IS NOT NULL
    ORDER BY t.trip_ID, a.departure_date;
    """

    result_rows = execute_query(query)

    if result_rows:
        display_report(result_rows)
    else:
        print("No data found.")