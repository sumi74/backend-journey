DROP TABLE if EXISTS customers;
create table if not EXISTS customers (
    id integer primary key AUTOINCREMENT,
    name text NOT NULL,
    city text NOT NULL
);

select * From customers;

INSERT INTO customers (name, city)
VALUES ('sumaya', 'nairobi');

SELECT * FROM customers;

INSERT INTO customers (name, city)
VALUES ('ahmed', 'mombasa');

SELECT * FROM customers;


insert into customers (name, city)
values ('amina', 'kisumu');
SELECT * FROM customers;

drop TABLE if EXISTS orders;
CREATE TABLE IF not EXISTS orders(
    id integer PRIMARY KEY AUTOINCREMENT,
    customer_id integer NOT NULL,
    product text not NULL,
    price real NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);
SELECT * FROM orders;

INSERT INTO orders (customer_id, product, price)
VALUES (1, 'laptop', 800);

SELECT * from orders;

INSERT into orders (customer_id, product, price)
VALUES(2, 'phone', 500);
SELECT * from orders;

INSERT INTO orders ( customer_id, product, price)
VALUES (1, 'keyboard', 50);
SELECT * from orders;

SELECT
    customers.name,
    orders.product,
    orders.price
FROM customers
JOIN orders
ON customers.id = orders.customer_id;



