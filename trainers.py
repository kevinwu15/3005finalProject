def loginTrainer(email, conn):
    with conn:
        with conn.cursor() as curs:
            curs.execute('SELECT * FROM trainers WHERE trainer_email = %s;', ((email,)))
            if curs.fetchall() == []:
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
                        curs.execute('SELECT first_name, last_name, member_email FROM members')
                        rows = curs.fetchall()
                        if rows != []:
                            for row in rows:
                                print(row[0] + " " + row[1])
                                print(row[2] + "\n")
                    case "3":
                        break
            curs.close()
            return False