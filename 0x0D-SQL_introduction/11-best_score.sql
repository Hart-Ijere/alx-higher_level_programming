-- Task: List all records with a score >= 10 in the table second_table from the database hbtn_0c_0
-- A query that selects and displays the score and name from rows where score is greater than or equal to 10,
-- ordered by score in descending order.

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
