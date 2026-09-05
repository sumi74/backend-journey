drop table if exists students;

create table if not exists students (
    id integer,
    name text,
    age integer,
    city text
);

insert into students (id, name, age, city)
values (1, 'sumaya', 20, 'nairobi');

insert  into students (id, name, age, city)
values (2, 'ahmed', 21, 'mombasa');

insert into students (id, name, age, city)
values (3, 'amine', 19, 'nairobi');

select * from students;

select name, city
from students;

select * from students
where city = 'nairobi';

select name, age
from students
where age >= 20;

update students
set city = 'kisumu'
where id = 3;

select * from students
where id = 3;

delete from students
where id = 2;

select * from students;

select * from students
order by age asc;

select * from students
order by age desc;

select * from students
limit 1;

select * from students
where age >= 20
and city = 'nairobi';

select * from students
where city = 'nairobi'
or city = 'kisumu';

select * from students
where city in ('nairobi', 'kisumu');


select * from students
where name like 'a%';

select * from students
where name like '%a';

select * from students
where name like '%m%';

select count(*) from students;

select count(*) as total_students
from students;

select min(age) as youngest
from students;

select max(age) as oldest
from students;

select avg(age) as average_age
from students;

select city, count(*) as total
from students
group by city;

select name, age, city
from students
where age >= 18
order by age desc 
limit 2;


select * from students
where age >= 20
and city = 'nairobi';

select * from students
where city = 'nairobi'
or city = 'kisumu';


select city
from students;

select distinct city
from students;

select name as student_name, age as student_age
from students;


select avg(age) as average_age
from students;


select city, count(*) as total
from students
group by city;

select city, count(*) as total
from students
group by city
having count(*) > 2;


create table courses (
    id integer,
    student_id integer,
    course text
);

insert into courses (id, student_id, course)
values(1, 1, 'python');

insert into courses (id, student_id, course)
values(2, 3, 'sql');

insert into courses (id, student_id, course)
values(3, 1, 'django');

select * from courses;



