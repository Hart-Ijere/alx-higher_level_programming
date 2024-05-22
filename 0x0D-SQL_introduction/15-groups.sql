-- Task: List the number of records with the same score in the table second_table from the database hbtn_0c_0
-- A query that selects the score and the count of records with that score, labeled as 'number',
-- and orders the results by the count in descending order.

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
