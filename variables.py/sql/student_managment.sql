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

INSERT INTO courses (name, teacher, fee)
VALUES
('python', 'mr.john', 300),
('sql', 'ms.sarah', 250),
('django','mr.david', 400),
('web development', 'ms.mary', 350);

SELECT * FROM courses;


INSERT INTO enrollments (student_id, course_id, grade)
VALUES
(1, 1, 85),
(1, 2, 90),
(2, 1, 72),
(2, 3, 80),
(3, 2, 88),
(3, 4, 91),
(4, 1, 95),
(4, 3, 87),
(5, 2, 76);

SELECT * FROM enrollments;


SELECT students.name
FROM students;


sELECT students.name
FROM students
JOIN enrollments
ON students.id = enrollments.student_id;

SELECT 
    students.name,
    courses.name
FROM students
JOIN enrollments
ON students.id = enrollments.student_id
JOIN courses
ON enrollments.course_id = courses.id;


SELECT
    students.name,
    courses.name,
    enrollments.grade
FROM students
JOIN enrollments
    ON students.id = enrollments.student_id
JOIN courses
    ON enrollments.course_id = courses.id;


SELECT 
    students.name,
    courses.name,
    enrollments.grade
FROM students
JOIN enrollments
    ON students.id = enrollments.student_id
JOIN courses
    ON enrollments.course_id = courses.id
WHERE enrollments.grade > 85;


SELECT 
    courses.name,
    avg(enrollments.grade) AS average_grade
FROM courses
JOIN enrollments
    ON courses.id = enrollments.course_id
GROUP BY courses.id;

SELECT 
    courses.name,
    count(enrollments.student_id) AS student_count
FROM courses
JOIN enrollments
    ON courses.id = enrollments.course_id
GROUP BY courses.id;


SELECT 
    courses.name,
    count(enrollments.student_id) AS student_count
FROM courses
JOIN enrollments
    ON courses.id = enrollments.course_id
GROUP BY courses.id
HAVING count(enrollments.student_id) > 2;

SELECT
    students.name,
    enrollments.grade
FROM students
JOIN enrollments
    ON students.id = enrollments.student_id
WHERE enrollments.grade = (SELECT max (grade) FROM enrollments);

SELECT 
    students.name,
    sum(courses.fee) AS total_paid
FROM students
JOIN enrollments
    ON students.id = enrollments.student_id
JOIN courses
    ON enrollments.course_id = courses.id
JOIN courses
    ON enrollments.course_id = courses.id
GROUP BY students.id, students.name;