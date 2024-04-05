def loginAdmin(email, conn):
    with conn:
        with conn.cursor() as curs:
            curs.execute('SELECT * FROM admin WHERE admin_email = %s;', ((email,)))
            if curs.fetchall() == []:
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
                        
                    case "9":
                        break
            curs.close()
            return False