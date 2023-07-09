import mysql.connector
from mysql.connector import errorcode

# Configure connection to DB
db = mysql.connector.connect(
    host = "127.0.0.1",
    database = "Outland_Adventure",
    user = "adventure_user",
    password = "adventure"

)

# Create cursor object to execute SQL queries
cursor = db.cursor()


try:
    #printing inoculations table
    print("--DISPLAYING inoculations RECORDS")
    cursor.execute("SELECT * FROM Inoculation")
    inoculations = cursor.fetchall()
    for inoculation in inoculations:
        print("Vaccine_ID: {}\nVaccine_Name: {}\nRecommended_Dosage: {}\nMedical_Information: {}\n".format
            (inoculation[0], inoculation[1], inoculation[2], inoculation[3]))

    #printing visa requirements table
    print("--DISPLAYING Visa Requirement RECORDS")

    cursor.execute("SELECT * FROM `Visa Requirements`")
    visas = cursor.fetchall()
    for visa in visas:
        print("Visa_Types: {}\nApplication_Process: {}\nVisa_Fees: {}\n".format
            (visa[0], visa[1], visa[2]))

    #printing locations table
    print("--DISPLAYING Location RECORDS")

    cursor.execute("SELECT * FROM Location")
    locations = cursor.fetchall()
    for location in locations:
        print("Location_ID: {}\nLocation_Name: {}\nLocation_Details: {}\nVaccine_ID: {}\nVisa_Type: {}\n".format
            (location[0], location[1], location[2], location[3],location[4]))

    #printing trips table
    print("--DISPLAYING Trip RECORDS")

    cursor.execute("SELECT * FROM Trip")
    trips = cursor.fetchall()
    for trip in trips:
        print("Trip ID: {}\nCustomer ID: {}\nVaccine ID: {}\nLocation ID:{}\n".format
            (trip[0], trip[1], trip[2], trip[3]))

    #printing equipments table
    print("--DISPLAYING Equipment RECORDS")

    cursor.execute("SELECT * FROM Equipment")
    equipments = cursor.fetchall()
    for equipment in equipments:
        print("Equipment ID: {}\nEquipment Name:{}\nEquipment Type:{}\nCustomer ID:{}\n".format
            (equipment[0], equipment[1], equipment[2], equipment[3]))

    #Printing department table
    print("--DISPLAYING department RECORDS")

    cursor.execute('SELECT * FROM Department')
    departments = cursor.fetchall()
    for department in departments:
        print("Department_name: {}\nDepartment_description: {}\nDepartment_email: {}\nDepartment_phone: {}\n".format
                (department[0], department[1], department[2], department[3]))

    #Printing Employee table   
    print("--DISPLAYING employee RECORDS")

    cursor.execute('SELECT * FROM Employee')
    employees = cursor.fetchall()
    for employee in employees:
        print("Employee_name: {}\nDepartment_ID {}\nEmployee_role: {}\nCustomer_bookings {}\n".format
                (employee[0], employee[1], employee[2], employee[3]))
        
    #Printing Airfare Table
    print("--DISPLAYING airfare RECORDS")

    cursor.execute('SELECT * FROM Airfare')
    airfares = cursor.fetchall()
    for airfare in airfares:
        print("Flight_number: {}\nArrival_date: {}\nDeparture_date: {}\nAirfare_costs: {}\nLocation_ID: {}\nTrip_ID {}\n".format
                (airfare[0], airfare[1], airfare[2], airfare[3], airfare[4], airfare[5]))
        
    #Printing Customer Order Table
    print("--DISPLAYING customer Order RECORDS")

    cursor.execute('SELECT * FROM `Customer Order`')
    orders = cursor.fetchall()
    for order in orders:
        print("Order_ID: {}\nEquipment_ID: {}\nEquipment_quantity: {}\nOrder_status: {}\nCustomer_ID: {}\nEmployee_ID {}\n".format
                (order[0], order[1], order[2], order[3], order[4], order[5]))
        
    #Printing Customers Table
    print("--DISPLAYING customers RECORDS")

    cursor.execute('SELECT * FROM customers')
    customers = cursor.fetchall()
    for customer in customers:
        print("Customer_ID: {}\nCustomer_name: {}\nCustomer_phone: {}\nCustomer_email: {}\nCustomer_address: {}\nCustomer_preferences: {}\nCustomer_requirements: {}\n".format
                (customer[0], customer[1], customer[2], customer[3], customer[4], customer[5], customer[6]))
    
except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("  the supplied username or password are invalid")
		
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("  The specific database does not exist")
	else:
		print (err)

finally:
	db.close()
	