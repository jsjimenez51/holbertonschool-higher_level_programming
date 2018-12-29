-- creates a table id_not_null on a MySQL server
-- id set to INT with value of 1
-- name set to VARCHAR(256)
CREATE TABLE IF NOT EXISTS id_not_null(
	id INT DEFAULT 1,
	name VARCHAR(256)
);
