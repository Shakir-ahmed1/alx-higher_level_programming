-- prints records which doesn't have a name with a NULL value
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
