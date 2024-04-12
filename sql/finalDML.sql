INSERT INTO members (member_email, member_password, first_name, last_name, height, curr_weight, goal_weight, goal_desc) VALUES ('member@email.com', 'member', 'Joe', 'Smith', 170, 135, 140, 'Gain muscle');

INSERT INTO trainers (trainer_email, trainer_password, first_name, last_name) VALUES ('trainer@email.com', 'trainer', 'Bob', 'Jones');

INSERT INTO admin (admin_email, admin_password, first_name, last_name) VALUES ('admin@email.com', 'admin', 'Admin', 'A');

INSERT INTO fitness_achievements (member_email, content) VALUES ('member@email.com', 'Gained 5 pounds!');

INSERT INTO training_sessions (trainer_email, timeslot, fee) VALUES ('trainer@email.com', '2024-04-05', 45);

INSERT INTO equipment (equipment_desc) VALUES ('Treadmill'), ('Chest press machine');

INSERT INTO payments (member_email, amount, payment_desc) VALUES ('member@email.com', '250', 'Registration');

INSERT INTO rooms (room_name) VALUES ('Room 1'), ('Room 2'), ('Room 3'), ('Room 4'), ('Room 5'), ('Room 6'), ('Room 7'), ('Room 8'), ('Room 9'), ('Room 10');

