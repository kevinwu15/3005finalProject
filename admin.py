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
                options = input("1. View Room Bookings\n2. Add Room Booking\n3. Remove Room Booking\n4. Modify Room Booking \n5. Monitor Equipment Maintenance\n6. New Equipment Maintenance\n7. Complete Equipment Maintenance\n8. View Group Classes\n9. Add Group Class\n10. Remove Group Class\n11. Modify Group Class\n12. Process Payments\n13. Log Out\n")
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
                                print("Time: " + str(row[2]) + "\n")

                    case "2":
                        curs.execute('SELECT * FROM rooms')
                        rows = curs.fetchall()
                        for row in rows:
                            print(row[1])
                            print("Room number: " + str(row[0]) + "\n")
                        room_num = input("Book which room number: ")
                        if not room_num.isdigit():
                            print("Invalid room number\n")
                            break
                        if int(room_num) < 1 or int(room_num) > 10:
                            print("Invalid room number\n")
                            break
                        date = input("Date of booked room session (in YYYY-MM-DD format): ")
                        time = input("Time of booked room session (in HH:MM format): ")
                        date_time = date + " " + time + ":00"
                        curs.execute('INSERT INTO room_bookings (room_number, timeslot, admin_email) VALUES (%s, %s, %s)', ((room_num, date_time, email)))
                        conn.commit()
                        print()
                    
                    case "3":
                        curs.execute('SELECT * FROM room_bookings')
                        rows = curs.fetchall()
                        if rows == []:
                            print("No rooms booked\n")
                        else:
                            for row in rows:
                                print("Booking ID: " + str(row[0]))
                                print("Room number: " + str(row[1]))
                                print("Time: " + str(row[2]) + "\n")
                        choice = input("Which room booking would you like to remove?: ")
                        curs.execute('DELETE FROM room_bookings WHERE booking_id = %s', ((choice,)))
                        conn.commit()
                        if curs.rowcount != 0:
                            print("Room booking deleted\n")
                        else:
                            print("Failed to delete room booking\n")
                    
                    case "4":
                        curs.execute('SELECT * FROM room_bookings')
                        rows = curs.fetchall()
                        if rows == []:
                            print("No rooms booked\n")
                        else:
                            for row in rows:
                                print("Booking ID: " + str(row[0]))
                                print("Room number: " + str(row[1]))
                                print("Time: " + str(row[2]) + "\n")
                        
                        choice = input("Which booking would you like to modify?: ")
                        if not choice.isdigit():
                            print("Invalid input\n")
                            break
                        curs.execute('SELECT * FROM room_bookings WHERE booking_id = %s', ((choice,)))
                        if curs.fetchall() == []:
                            print("Invalid Booking ID\n")
                            break
                        print("Update info below")
                        room_num = input("Room number: ")
                        if not room_num.isdigit():
                            print("Invalid room number\n")
                            break
                        if int(room_num) < 1 or int(room_num) > 10:
                            print("Invalid room number\n")
                            break
                        date = input("Date of booked room session (in YYYY-MM-DD format): ")
                        time = input("Time of booked room session (in HH:MM format): ")
                        date_time = date + " " + time + ":00"
                        curs.execute('UPDATE room_bookings SET room_number = %s, timeslot = %s WHERE booking_id = %s', ((room_num, date_time, choice)))
                        conn.commit()
                        print()
                    
                    case "5":
                        curs.execute('SELECT * FROM equipment_maintenance')
                        rows = curs.fetchall()
                        if rows == []:
                            print("No equipment under maintenance\n")
                        else:
                            for row in rows:
                                print("Equipment ID: " + str(row[0]))
                                curs.execute('SELECT equipment_desc FROM equipment WHERE equipment_id = %s', ((row[0],)))
                                print(curs.fetchone()[0])
                                print("Maintenance start date: " + str(row[1]) + "\n")
                    
                    case "6":
                        curs.execute('SELECT equipment.* FROM equipment LEFT JOIN equipment_maintenance ON equipment.equipment_id = equipment_maintenance.equipment_id WHERE equipment_maintenance.equipment_id IS NULL')
                        rows = curs.fetchall()
                        if rows == []:
                            print("No working equipment\n")
                        else:
                            for row in rows:
                                print("Equipment ID: " + str(row[0]))
                                print(row[1] + "\n")
                        equipment_id = input("Equipment ID: ")
                        date = input("Maintenance start date (in YYYY-MM-DD format): ")
                        curs.execute('INSERT INTO equipment_maintenance (equipment_id, date_start, admin_email) VALUES (%s, %s, %s)', ((equipment_id, date, email)))
                        conn.commit()
                        print("Successfully added maintenance\n")
                    
                    case "7":
                        curs.execute('SELECT * FROM equipment_maintenance')
                        rows = curs.fetchall()
                        if rows == []:
                            print("No equipment under maintenance\n")
                        else:
                            for row in rows:
                                print("Maintenance ID: " + str(row[0]))
                                curs.execute('SELECT equipment_desc FROM equipment WHERE equipment_id = %s', ((row[0],)))
                                print(curs.fetchone()[0])
                                print("Maintenance start date: " + str(row[1]) + "\n")
                        choice = input("Which maintenance should be marked as complete?: ")
                        if not choice.isdigit():
                            print("Invalid input\n")
                            break
                        curs.execute('DELETE FROM equipment_maintenance WHERE equipment_id = %s', ((choice,)))
                        conn.commit()
                        print()
                        
                    case "8":
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
                                print()
                        print()
                    
                    case "9":
                        session_name = input("Session name: ")
                        date = input("Date of group session (in YYYY-MM-DD format): ")
                        time = input("Time of group session (in HH:MM format): ")
                        session_time = date + " " + time + ":00"
                        curs.execute('INSERT INTO group_sessions (session_name, timeslot, admin_email) VALUES (%s, %s, %s)', ((session_name, session_time, email)))
                        conn.commit()
                        print("Session added\n")
                    
                    case "10":
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
                    
                    case "11":
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
                        choice = input("Which session should be modified?: ")
                        if not choice.isdigit():
                            print("Invalid input\n")
                            break
                        session_name = input("Session name: ")
                        date = input("Date of group session (in YYYY-MM-DD format): ")
                        time = input("Time of group session (in HH:MM format): ")
                        session_time = date + " " + time + ":00"
                        curs.execute('UPDATE group_sessions SET session_name = %s, timeslot = %s WHERE session_id = %s', ((session_name, session_time, choice)))
                        conn.commit()
                        print("Updated session\n")

                    case "12":
                        curs.execute('SELECT * FROM payments WHERE admin_email IS NULL')
                        rows = curs.fetchall()
                        if rows == []:
                            print("No payments to process\n")
                            break 
                        else:
                            for row in rows:
                                print("Payment ID: " + str(row[0]))
                                print(row[3] + " Fee")
                                print(row[1])
                                print("$" + str(row[2]) + "\n")
                        choice = input("Which payment should be processed?: ")
                        if not choice.isdigit():
                            print("Invalid input\n")
                            break
                        curs.execute('UPDATE payments SET admin_email = %s WHERE payment_id = %s', ((email, choice)))
                        conn.commit()
                        print()

                    case "13":
                        break
            curs.close()
            return False