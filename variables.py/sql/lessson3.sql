create table if not exists employees (
    id integer primary key,
    name text,
    age integer
);

select * from employees;
insert into employees (id, name, age)
values (1, 'ali', 25);

delete from employees;
select * from employees;



create table products (
    id integer primary key,
    name text,
    price integer
);

insert into products (name, price)
values ('laptop', 800);

select * from products;

