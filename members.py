from config import parseCursorFetch
import datetime

def registerMember(email, first_name, last_name, conn):
    with conn:
        with conn.cursor() as curs:
            curs.execute('SELECT * FROM members WHERE member_email = %s;', ((email,)))
            if curs.fetchall() != []:
                curs.close()
                return False
            curs.execute('INSERT INTO members (member_email, first_name, last_name) VALUES (%s, %s, %s);', ((email, first_name, last_name)))
            curs.close()
            return True

def loginMember(email, conn):
    with conn:
        with conn.cursor() as curs:
            curs.execute('SELECT * FROM members WHERE member_email = %s;', ((email,)))
            if curs.fetchall() == []:
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
                        curs.execute('SELECT (first_name, last_name, member_email, height, curr_weight) FROM members WHERE member_email = %s', ((email,)))
                        print(curs.fetchone()[0])
                    case "2":
                        height = input("Height: ")
                        weight = input("Weight: ")
                        curs.execute('UPDATE members SET height = %s, curr_weight = %s WHERE member_email = %s', ((height, weight, email)))
                    case "3":
                        curs.execute('SELECT (goal_weight, goal_desc) FROM members WHERE member_email = %s', ((email,)))
                        print(curs.fetchone()[0])
                    case "4":
                        goal_weight = input("Goal Weight: ")
                        goal_desc = input("Goal Description: ")
                        curs.execute('UPDATE members SET goal_weight = %s, goal_desc = %s WHERE member_email = %s', ((goal_weight, goal_desc, email)))
                    case "5":
                        print("FITNESS ACHIEVEMENTS")
                    case "7":
                        curs.execute('SELECT * FROM training_sessions WHERE member_email IS NULL')
                        rows = curs.fetchall()
                        for row in rows:
                            print("Session ID: " + str(row[0]))
                            print("Trainer: " + row[1])
                            print("Time: " + str(row[2]) + "\n")
                    case "10":
                        break
            return False
