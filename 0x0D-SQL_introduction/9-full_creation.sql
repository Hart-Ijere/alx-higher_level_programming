-- Task: Create a table called second_table in the database hbtn_0c_0 and add multiple rows
-- This query creates the table second_table with columns id, name, and score if it does not already exist,
-- and inserts multiple rows into the table.

CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10), (2, 'Alex', 3), (3, 'Bob', 14), (4, 'George', 8);
