def registerMember(email, first_name, last_name, conn):
    with conn:
        with conn.cursor() as curs:
            curs.execute('SELECT * FROM members WHERE member_email = %s;', ((email,)))
            if curs.fetchall() != []:
                curs.close()
                return False
            password = input("Set password: ")
            curs.execute('INSERT INTO members (member_email, member_password, first_name, last_name) VALUES (%s, %s, %s, %s);', ((email, password, first_name, last_name)))
            curs.execute('INSERT INTO payments (member_email, amount, payment_desc) VALUES (%s, %s, %s)', ((email, 250, "Registration")))
            curs.close()
            return True

def loginMember(email, conn):
    with conn:
        with conn.cursor() as curs:
            curs.execute('SELECT * FROM members WHERE member_email = %s;', ((email,)))
            if curs.fetchall() == []:
                curs.close()
                return False
            password = input("Enter password: ")
            curs.execute('SELECT member_password FROM members WHERE member_email = %s', ((email,)))
            row = curs.fetchone()
            if password != row[0]:
                curs.close()
                return False
            curs.close()
            return True

def memberDashboard(email, conn):
    print("Welcome Member %s!" % email)
    with conn:
        with conn.cursor() as curs:
            while True:
                options = input("1. View Personal Information + Health Metrics\n2. Update Personal Information + Health Metrics\n3. View Fitness Goals\n4. Update Fitness Goals\n5. View Fitness Achievements\n6. View Exercise Routines\n7. Book Personal Training\n8. Cancel Personal Training\n9. Book Group Classes\n10. Log Out\n")
                match options:
                    case "1":
                        curs.execute('SELECT first_name, last_name, member_email, height, curr_weight FROM members WHERE member_email = %s', ((email,)))
                        row = curs.fetchone()
                        print(row[0] + " " + row[1])
                        print(row[2])
                        print("Height: " + str(row[3]))
                        print("Weight: " + str(row[4]) + "\n")

                    case "2":
                        height = input("Height: ")
                        weight = input("Weight: ")
                        print()
                        curs.execute('UPDATE members SET height = %s, curr_weight = %s WHERE member_email = %s', ((height, weight, email)))
                        conn.commit()

                    case "3":
                        curs.execute('SELECT goal_weight, goal_desc FROM members WHERE member_email = %s', ((email,)))
                        row = curs.fetchone()
                        print("Goal Weight: " + str(row[0]))
                        print("Goal Description: " + str(row[1]) + "\n")

                    case "4":
                        goal_weight = input("Goal Weight: ")
                        goal_desc = input("Goal Description: ")
                        print()
                        curs.execute('UPDATE members SET goal_weight = %s, goal_desc = %s WHERE member_email = %s', ((goal_weight, goal_desc, email)))
                        conn.commit()

                    case "5":
                        curs.execute('SELECT content FROM fitness_achievements WHERE member_email = %s', ((email,)))
                        rows = curs.fetchall()
                        if rows != []:
                            for row in rows:
                                print(row[0])
                        print()

                    case "6":
                        curs.execute('SELECT * FROM training_sessions WHERE member_email = %s', ((email,)))
                        print("Registered Personal Training Sessions")
                        rows = curs.fetchall()
                        for row in rows:
                            print("Session ID: " + str(row[0]))
                            print("Trainer: " + row[1])
                            print("Time: " + str(row[2]) + "\n")
                        
                        curs.execute('SELECT * FROM group_session_registered WHERE member_email = %s', ((email,)))
                        print("Registered Group Sessions")
                        rows = curs.fetchall()
                        for row in rows:
                            curs.execute('SELECT * FROM group_sessions WHERE session_id = %s', ((row[0],)))
                            data = curs.fetchone()
                            print("Session ID: " + str(data[0]))
                            print("Session Name: " + data[1])
                            print("Time: "+ str(data[2]) + "\n")

                    case "7":
                        curs.execute('SELECT * FROM training_sessions WHERE member_email IS NULL')
                        rows = curs.fetchall()
                        if rows != []:
                            for row in rows:
                                print("Session ID: " + str(row[0]))
                                print("Trainer: " + row[1])
                                print("Fee: $" + str(row[4]))
                                print("Time: " + str(row[2]) + "\n")
                            choice = input("Which session would you like to book?: ")
                            curs.execute('SELECT * FROM training_sessions WHERE session_id = %s', ((choice,)))
                            if curs.fetchall() != []:
                                curs.execute('SELECT fee FROM training_sessions WHERE session_id = %s', ((choice,)))
                                fee = curs.fetchone()[0]
                                curs.execute('UPDATE training_sessions SET member_email = %s WHERE session_id = %s', ((email, choice)))
                                curs.execute('INSERT INTO payments (member_email, amount, payment_desc) VALUES (%s, %s, %s)', ((email, fee, "Personal Training")))
                                conn.commit()
                                print("Successfully booked this session!\n")
                            else:
                                print("Session ID invalid\n")
                        else:
                            print("No available sessions\n")
                    
                    case "8":
                        curs.execute('SELECT * FROM training_sessions WHERE member_email = %s', ((email,)))
                        print("Registered Personal Training Sessions")
                        rows = curs.fetchall()
                        for row in rows:
                            print("Session ID: " + str(row[0]))
                            print("Trainer: " + row[1])
                            print("Time: " + str(row[2]) + "\n")
                        choice = input("Cancel which session?: ")
                        curs.execute('SELECT * FROM training_sessions WHERE session_id = %s AND member_email = %s', ((choice, email)))
                        if curs.fetchall() != []:
                            curs.execute('UPDATE training_sessions SET member_email = NULL WHERE session_id = %s', ((choice,)))
                            conn.commit()
                            print("Successfully cancelled this session\n")
                        else:
                            print("Session ID invalid\n")
                    
                    case "9":
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
                        
                        choice = input("Book which session?: ")
                        if not choice.isdigit():
                            print("Invalid input\n")
                            break
                        curs.execute('SELECT * FROM group_sessions WHERE session_id = %s', ((choice)))
                        if curs.fetchall() == []:
                            print("Invalid Session ID")
                            break
                        curs.execute('INSERT INTO group_session_registered (session_id, member_email) VALUES (%s, %s)', ((choice, email)))
                        conn.commit()
                        print("Successfully booked this group session!\n")
                    case "10":
                        break
            curs.close()
            return False
