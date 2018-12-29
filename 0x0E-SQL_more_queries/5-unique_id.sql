-- creates a table called unique_id on a MySQL server
-- id set to INT with default value of 1 that is unique
-- name set to VARCHAR(256)
CREATE TABLE unique_id (
id INT DEFAULT 1 UNIQUE,
name VARCHAR(256)
);
