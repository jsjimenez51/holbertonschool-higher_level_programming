-- lists all the related data in a table found in a MySQL database
-- record to be found is California but ids can be different
-- results must be sorted in ascending order
SELECT 'id', 'name'
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id ASC;
