DROP TABLE if EXISTS book;
CREATE TABLE IF NOT EXISTS books  (
    id integer PRIMARY KEY AUTOINCREMENT,
    title text not null,
    author text not null,
    price real,
    status text DEFAULT 'available'
);

INSERT INTO books (title, author, price)
VALUES ('book 1', 'sumi',2.2);

INSERT into books ( title author, price)
VALUES('book 3', 'sami', 5.1);

SELECT * FROM books;
