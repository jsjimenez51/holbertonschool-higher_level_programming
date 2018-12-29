-- creates the database hbtn_0d_usa and table states on server
-- states desc: id INT unique, auto gen, not null, and primary key
-- name VC256 not null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0hbtn_0d_usa.states (
	id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
