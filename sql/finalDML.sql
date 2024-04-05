INSERT INTO members (member_email, first_name, last_name, height, curr_weight, goal_weight, goal_desc) VALUES ('testmember@email.com', 'Joe', 'Smith', 170, 135, 140, 'Gain muscle');

INSERT INTO trainers (trainer_email, first_name, last_name) VALUES ('trainer@email.com', 'Bob', 'Jones');

INSERT INTO admin (admin_email, first_name, last_name) VALUES ('admin@email.com', 'Admin', 'A');

INSERT INTO fitness_achievements (member_email, content) VALUES ('testmember@email.com', 'Gained 5 pounds!');

INSERT INTO training_sessions (trainer_email, timeslot, fee) VALUES ('trainer@email.com', '2024-04-05', 45);

INSERT INTO equipment_maintenance (equipment_desc, date_start) VALUES ('Broken treadmill', '2024-04-04'), ('Broken Smith machine', '2024-04-03');

