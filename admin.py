def loginAdmin(email, conn):
    with conn:
        with conn.cursor() as curs:
            curs.execute('SELECT * FROM admin WHERE admin_email = %s;', ((email,)))
            if curs.fetchall() == []:
                curs.close()
                return False
            password = input("Enter password: ")
            curs.execute('SELECT admin_password FROM admin WHERE admin_email = %s', ((email,)))
            row = curs.fetchone()
            if password != row[0]:
                curs.close()
                return False
            curs.close()
            return True

def adminDashboard(email, conn):
    print("Welcome Admin %s!" % email)
    with conn:
        with conn.cursor() as curs:
            while True:
                options = input("1. View Room Bookings\n2. Add Room Booking\n3. Remove Room Booking\n4. Monitor Equipment Maintenance\n5. View Group Classes\n6. Add Group Class\n7. Remove Group Class\n8. Process Payments\n9. Log Out\n")
                match options:
                    case "1":
                        curs.execute('SELECT * FROM room_bookings')
                        rows = curs.fetchall()
                        if rows == []:
                            print("No rooms booked\n")
                        else:
                            for row in rows:
                                print("Booking ID: " + str(row[0]))
                                print("Room number: " + str(row[1]))
                                print("Booked by: " + row[2])
                                print("Time: " + str(row[3]) + "\n")

                    case "2":
                        room_num = input("Room number: ")
                        if not room_num.isdigit():
                            print("Invalid room number\n")
                            break
                        if int(room_num) < 1 or int(room_num) > 10:
                            print("Invalid room number\n")
                            break
                        member_email = input("Member email: ")
                        date = input("Date of booked room session (in YYYY-MM-DD format): ")
                        time = input("Time of booked room session (in HH:MM format): ")
                        date_time = date + " " + time + ":00"
                        curs.execute('SELECT * FROM members WHERE member_email = %s', ((member_email,)))
                        if curs.rowcount != 0:
                            curs.execute('INSERT INTO room_bookings (room_number, member_email, timeslot) VALUES (%s, %s, %s)', ((room_num, member_email, date_time)))
                            conn.commit()
                            print("Successfully added room booking!\n")
                        else:
                            print("Could not book room, invalid member email\n")
                    
                    case "3":
                        curs.execute('SELECT * FROM room_bookings')
                        rows = curs.fetchall()
                        if rows == []:
                            print("No rooms booked\n")
                        else:
                            for row in rows:
                                print("Booking ID: " + str(row[0]))
                                print("Room number: " + str(row[1]))
                                print("Booked by: " + row[2])
                                print("Time: " + str(row[3]) + "\n")
                        choice = input("Which room booking would you like to remove?: ")
                        curs.execute('DELETE FROM room_bookings WHERE booking_id = %s', ((choice,)))
                        conn.commit()
                        if curs.rowcount != 0:
                            print("Room booking deleted\n")
                        else:
                            print("Failed to delete room booking\n")
                    
                    case "4":
                        curs.execute('SELECT * FROM equipment_maintenance')
                        rows = curs.fetchall()
                        if rows == []:
                            print("No equipment under maintenance\n")
                        else:
                            for row in rows:
                                print(row[0])
                                print("Maintenance start date: " + str(row[1]) + "\n")
                    
                    case "5":
                        curs.execute('SELECT * FROM group_sessions')
                        rows = curs.fetchall()
                        if rows == []:
                            print("No group sessions\n")
                        else:
                            for row in rows:
                                print(row[1])
                                print(str(row[2]))
                                curs.execute('SELECT member_email FROM group_session_registered WHERE session_id = %s', ((row[0],)))
                                print("Registered members:")
                                print(curs.fetchall())
                    
                    case "6":
                        session_name = input("Session name: ")
                        date = input("Date of group session (in YYYY-MM-DD format): ")
                        time = input("Time of group session (in HH:MM format): ")
                        session_time = date + " " + time + ":00"
                        curs.execute('INSERT INTO group_sessions (session_name, timeslot) VALUES (%s, %s)', ((session_name, session_time)))
                        conn.commit()
                        print("Session added\n")
                    
                    case "7":
                        curs.execute('SELECT * FROM group_sessions')
                        rows = curs.fetchall()
                        if rows == []:
                            print("No group sessions\n")
                            break
                        else:
                            for row in rows:
                                print("Session ID: " + str(row[0]))
                                print(row[1])
                                print(str(row[2]) + "\n")
                        choice = input("Which session should be removed?: ")
                        if not choice.isdigit():
                            print("Invalid input\n")
                            break
                        curs.execute('DELETE FROM group_session_registered WHERE session_id = %s', ((choice,)))
                        curs.execute('DELETE FROM group_sessions WHERE session_id = %s', ((choice,)))
                        conn.commit()
                        print()

                    case "8":
                        curs.execute('SELECT * FROM payments')
                        rows = curs.fetchall()
                        if rows == []:
                            print("No payments to process\n")
                            break 
                        else:
                            for row in rows:
                                print("Payment ID: " + str(row[0]))
                                print(row[1])
                                print("$" + str(row[2]))
                        choice = input("Which payment should be processed?: ")
                        if not choice.isdigit():
                            print("Invalid input\n")
                            break
                        curs.execute('DELETE FROM payments WHERE payment_id = %s', ((choice,)))

                    case "9":
                        break
            curs.close()
            return False