drop table if exists teachers;

create table if not exists teachers (
    id integer,
    name text,
    subject text
);

insert into teachers (id, name, subject)
values (1, 'ali', 'math');

insert into teachers (id, name, subject)
values (2, 'amina', NULL);

insert into teachers (id, name, subject)
values (3, 'ahmed', 'english');

select * from teachers;


select * from teachers
where subject is null;

