CREATE TABLE members (
    member_email VARCHAR(255) PRIMARY KEY,
    member_password VARCHAR(255) NOT NULL,
	first_name VARCHAR(255) NOT NULL,
	last_name VARCHAR(255) NOT NULL,
    height INT,
    curr_weight INT,
    goal_weight INT,
    goal_desc TEXT
);

CREATE TABLE trainers (
    trainer_email VARCHAR(255) PRIMARY KEY,
    trainer_password VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
	last_name VARCHAR(255) NOT NULL
);

CREATE TABLE admin (
    admin_email VARCHAR(255) PRIMARY KEY,
    admin_password VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
	last_name VARCHAR(255) NOT NULL
);

CREATE TABLE fitness_achievements (
    member_email VARCHAR(255),
    FOREIGN KEY (member_email) REFERENCES members(member_email),
    content TEXT
);

CREATE TABLE training_sessions (
    session_id SERIAL PRIMARY KEY,
    trainer_email VARCHAR(255),
    FOREIGN KEY (trainer_email) REFERENCES trainers(trainer_email),
    timeslot TIMESTAMP NOT NULL,
    member_email VARCHAR(255),
    FOREIGN KEY (member_email) REFERENCES members(member_email),
    fee NUMERIC NOT NULL
);

CREATE TABLE rooms (
    room_number SERIAL PRIMARY KEY,
    room_name TEXT
);

CREATE TABLE room_bookings (
    booking_id SERIAL PRIMARY KEY,
    room_number INT,
    FOREIGN KEY (room_number) REFERENCES rooms(room_number),
    CONSTRAINT CHK_ValidRoomNum CHECK (room_number >= 1 AND room_number <= 10),
    timeslot TIMESTAMP NOT NULL,
    admin_email VARCHAR(255),
    FOREIGN KEY (admin_email)  REFERENCES admin(admin_email)
);

CREATE TABLE equipment (
    equipment_id SERIAL PRIMARY KEY,
    equipment_desc TEXT NOT NULL
);

CREATE TABLE equipment_maintenance (
    equipment_id INT,
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id),
    date_start DATE NOT NULL,
    admin_email VARCHAR(255),
    FOREIGN KEY (admin_email) REFERENCES admin(admin_email)
);

CREATE TABLE group_sessions (
    session_id SERIAL PRIMARY KEY,
    session_name VARCHAR(255) NOT NULL,
    timeslot TIMESTAMP NOT NULL,
    admin_email VARCHAR(255),
    FOREIGN KEY (admin_email) REFERENCES admin(admin_email)
);

CREATE TABLE group_session_registered (
    session_id INT,
    FOREIGN KEY (session_id) REFERENCES group_sessions(session_id),
    member_email VARCHAR(255),
    FOREIGN KEY (member_email) REFERENCES members(member_email)
);

CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    member_email VARCHAR(255),
    FOREIGN KEY (member_email) REFERENCES members(member_email),
    amount NUMERIC NOT NULL,
    payment_desc TEXT,
    admin_email VARCHAR(255),
    FOREIGN KEY (admin_email) REFERENCES admin(admin_email)
);