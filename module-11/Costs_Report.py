import mysql.connector
from mysql.connector import errorcode

# Configure connection to DB
db_config = {
    "host": "127.0.0.1",
    "user": "adventure_user",
    "password": "adventure",
    "database": "Outland_Adventure",
}

def execute_query(query, params=None):
    with mysql.connector.connect(**db_config) as connection:
        # Create cursor object to execute SQL queries
        cursor = connection.cursor()

        # Connect to Database
        try:
            cursor.execute(query, params)
            while True:
                row = cursor.fetchone()
                if row is None:
                    break
                yield row
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()

def display_report(rows):
    # Display Report title
    print("--- Total Costs for Outland Adventures ---")
    # Display Header
    print("Trip ID | Airfare Costs | Visa Fees")
    print("-" * 110)

    for row in rows:
        trip_ID, airfare_cost, visa_fees = row
        print(f"{trip_ID} | {airfare_cost} | {visa_fees}")

if __name__ == "__main__":
    query = """
    SELECT t.trip_ID, a.airfare_cost, vr.visa_fees
    FROM trip t
    JOIN airfare a ON t.trip_ID = a.trip_ID
    JOIN `customer order` co ON t.customer_ID = co.customer_ID
    JOIN location l ON t.location_ID = l.location_ID
    LEFT JOIN `visa requirements` vr ON l.visa_type = vr.visa_type
    WHERE t.trip_ID IS NOT NULL
    ORDER BY t.trip_ID;
    """

    result_rows = execute_query(query)

    if result_rows:
        display_report(result_rows)
    else:
        print("No data found.")
