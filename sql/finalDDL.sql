CREATE TABLE members (
    member_email VARCHAR(255) PRIMARY KEY,
	first_name VARCHAR(255) NOT NULL,
	last_name VARCHAR(255) NOT NULL,
    height INT,
    curr_weight INT,
    goal_weight INT,
    goal_desc TEXT
);

CREATE TABLE trainers (
    trainer_email VARCHAR(255) PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
	last_name VARCHAR(255) NOT NULL
);

CREATE TABLE admin (
    admin_email VARCHAR(255) PRIMARY KEY,
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
    timeslot TIMESTAMP,
    member_email VARCHAR(255),
    FOREIGN KEY (member_email) REFERENCES members(member_email),
);

CREATE TABLE room_bookings (
    booking_ID SERIAL PRIMARY KEY,
    room_number INT,
    CONSTRAINT CHK_ValidRoomNum CHECK (room_number >= 1 AND room_number <= 10),
    member_email VARCHAR(255),
    FOREIGN KEY (member_email) REFERENCES members(member_email),
    timeslot TIMESTAMP
);