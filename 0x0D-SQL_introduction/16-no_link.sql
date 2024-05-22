-- Task: List all records of the table second_table from the database hbtn_0c_0, excluding rows without a name value
-- A query that selects and displays the score and name from all rows with a non-null name,
-- ordered by score in descending order.

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
