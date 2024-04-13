INSERT INTO members (member_email, member_password, first_name, last_name, height, curr_weight, goal_weight, goal_desc) VALUES ('member@email.com', 'member', 'Joe', 'Smith', 170, 135, 140, 'Gain muscle');

INSERT INTO trainers (trainer_email, trainer_password, first_name, last_name) VALUES ('trainer@email.com', 'trainer', 'Bob', 'Jones');

INSERT INTO admin (admin_email, admin_password, first_name, last_name) VALUES ('admin@email.com', 'admin', 'Admin', 'A');

INSERT INTO fitness_achievements (member_email, content) VALUES ('member@email.com', 'Gained 5 pounds!');

INSERT INTO training_sessions (trainer_email, timeslot, fee) VALUES ('trainer@email.com', '2024-04-14 18:00', 25), ('trainer@email.com', '2024-04-16 14:00', 30);

INSERT INTO group_sessions (session_name, timeslot, admin_email) VALUES ('Group Cardio', '2024-04-14 19:00', 'admin@email.com'), ('Yoga', '2024-04-16 13:00', 'admin@email.com');

INSERT INTO equipment (equipment_desc) VALUES ('Treadmill'), ('Chest Press machine'), ('Row Machine'), ('Squat Rack');

INSERT INTO payments (member_email, amount, payment_desc) VALUES ('member@email.com', '250', 'Registration');

INSERT INTO rooms (room_name) VALUES ('Yoga Room'), ('Cardio Room'), ('Boxing Room'), ('Posing Room'), ('Yoga Room 2'), ('Stretching Room'), ('Massage Room'), ('Cardio Room 2'), ('Boxing Room 2'), ('Empty Room');

