def loginTrainer(email, conn):
    with conn:
        with conn.cursor() as curs:
            curs.execute('SELECT * FROM trainers WHERE trainer_email = %s;', ((email,)))
            if curs.fetchall() == []:
                curs.close()
                return False
            password = input("Enter password: ")
            curs.execute('SELECT trainer_password FROM trainers WHERE trainer_email = %s', ((email,)))
            row = curs.fetchone()
            if password != row[0]:
                curs.close()
                return False
            curs.close()
            return True

def trainerDashboard(email, conn):
    print("Welcome Trainer %s!" % email)
    with conn:
        with conn.cursor() as curs:
            while True:
                options = input("1. Open new Training session\n2. Member search\n3. Log Out\n")
                match options:
                    case "1":
                        date = input("Date of training session (in YYYY-MM-DD format): ")
                        time = input("Time of training session (in HH:MM format): ")
                        date_time = date + " " + time + ":00"
                        fee = input("Fee: ")
                        curs.execute('INSERT INTO training_sessions (trainer_email, timeslot, fee) VALUES (%s, %s, %s)', ((email, date_time, fee)))
                        conn.commit()
                    case "2":
                        name = input("Member to search (Last name): ")
                        curs.execute('SELECT first_name, last_name, height, curr_weight FROM members WHERE last_name = %s', ((name,)))
                        rows = curs.fetchall()
                        if rows != []:
                            for row in rows:
                                print(row[0] + " " + row[1])
                                print("Height: " + str(row[2]))
                                print("Weight: " + str(row[3]) + "\n")
                        else:
                            print("No such users")
                    case "3":
                        break
            curs.close()
            return False