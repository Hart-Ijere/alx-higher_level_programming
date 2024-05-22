-- Task: Compute the score average of all records in the table second_table from the database hbtn_0c_0
-- A query that calculates the average score of all rows, with the result column named 'average'.

SELECT AVG(score) AS average FROM second_table;
