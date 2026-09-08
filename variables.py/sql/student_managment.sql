DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS courses;
DROP TABLE if EXISTS enrollments;


CREATE table if NOT EXISTS students (
    id integer PRIMARY KEY AUTOINCREMENT,
    name text NOT NULL,
    age integer NOT NULL,
    city text NOT NULL
);

CREATE table if NOT EXISTS courses (
    id integer PRIMARY KEY AUTOINCREMENT,
    name text NOT NULL,
    teacher text NOT NULL,
    fee real NOT NULL
);

create TABLE IF NOT EXISTS enrollments (
    id integer PRIMARY KEY AUTOINCREMENT,
    student_id integer NOT NULL,
    course_id integer NOT NULL,
    grade real,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);

INSERT INTO students (name, age, city)
VALUES
('sumaya', 20, 'nairobi'),
('ahmed', 21, 'mombasa'),
('amina', 19, 'kisumu'),
('ali', 22, 'nairobi'),
('hassan', 20, 'nakuru');

SELECT * FROM students;



