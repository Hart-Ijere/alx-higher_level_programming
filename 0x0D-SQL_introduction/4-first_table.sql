-- Task: Create a table called first_table in the current database in your MySQL server
-- A query that creates the table first_table with columns id and name if it does not already exist.

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
