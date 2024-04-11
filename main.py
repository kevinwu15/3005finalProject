import psycopg2
from config import getFields
from members import *
from trainers import *
from admin import *

if __name__ == "__main__":
    # Attempting to connect to the database by using the psycopg2 connect
    try:
        # Using the getFields function from config.py to access information stored in the database.ini file
        fields = getFields()
        print("Connecting to Health and Fitness Database Management System")
        # Unpacking the fields dictionary into parameters for the connect function
        # trying to assign a new connection
        conn = psycopg2.connect(**fields)
        # Prompt user to call functions
        loggedIn = False
        while not loggedIn:
            option = input("Welcome to the Health and Fitness Database Management System!\n1. Register as a Member\n2. Member Login\n3. Trainer Login\n4. Admin Login\n5. Exit\n")
            match option:
                case "1":
                    email = input("Email: ")
                    first_name = input("First Name: ")
                    last_name = input("Last name: ")
                    if registerMember(email, first_name, last_name, conn):
                        print("Successfully registered!\n")
                    else:
                        print("The email is already in use, login instead\n")
                case "2":
                    email = input("Email: ")
                    loggedIn = loginMember(email, conn)
                    if loggedIn:
                        print("Successfully logged in as %s\n" % email)
                        loggedIn = memberDashboard(email, conn)
                    else:
                        print("Unsuccessful login\n")
                case "3":
                    email = input("Email: ")
                    loggedIn = loginTrainer(email, conn)
                    if loggedIn:
                        print("Successfully logged in as %s\n" % email)
                        loggedIn = trainerDashboard(email, conn)
                    else:
                        print("Unsuccessful login\n")
                case "4":
                    email = input("Email: ")
                    loggedIn = loginAdmin(email, conn)
                    if loggedIn:
                        print("Successfully logged in as %s\n" % email)
                        loggedIn = adminDashboard(email, conn)
                    else:
                        print("Unsuccessful login\n")
                case "5":
                    # Exit loop
                    loggedIn = True

    # Catch error if database connection unsuccessful
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    # Close connection to database at the end
    finally:
        print("Closing connection to database")
        conn.close()