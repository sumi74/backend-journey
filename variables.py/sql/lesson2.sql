drop table if exists products;
drop table if exists accounts;
drop table if exists users;
drop table if exists tasks;
drop table IF EXISTS enrollments;
DROP table if exists orders;
create table if not exists products (
    id integer primary key autoincrement,
    name text,
    price real
);

insert into products (name, price)
values ('laptop', 800);

select * from products;

insert into products (name, price)
values ('phone', 500);

select * from products;

create table if not exists accounts (
    id integer primary key autoincrement,
    username text not null,
    email text not null
);

insert into accounts (username, email)
values ('sumaya', 'sumaya@example.com');

select * from accounts;


create table if not exists users (
    id integer primary key autoincrement,
    username text unique,
    email text unique
);
 insert into users (username, email)
 values ('sumaya', 'sumaya@example.com');

select * from users;


create table if not exists tasks (
    id integer primary key autoincrement,
    title text not null,
    status text default 'pending'
);

insert into tasks (title)
values ('learn SQL');

select * from tasks;


create table if not exists enrollments (
    id integer primary key autoincrement,
    student_id integer,
    course_name text,
    foreign key (student_id) REFERENCES students(id)
);

insert into enrollments ( student_id, course_name)
VALUES (1, 'python');

select * from enrollments;

CREATE table if not EXISTS orders (
    id integer PRIMARY key AUTOINCREMENT,
    customer_name text not null,
    product text not null,
    status text DEFAULT 'pending'
);

INSERT into orders (customer_name, product)
VALUES ('sumaya', 'laptop');

insert into orders (customer_name, product, status)
values ('ahmed', 'phone', 'completed');

SELECT * FROM orders;

