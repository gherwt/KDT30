-- practice03.sql

USE practice;

CREATE TABLE employees(
	id INT PRIMARY KEY AUTO_INCREMENT,
    last_name VARCHAR(20) NOT NULL,
    first_name VARCHAR(20) NOT NULL,
    middle_name VARCHAR(20),
    age int NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'working'
);

INSERT INTO employees(first_name, last_name, age) 
VALUES 
	-- ('Dora', 'Smith', 58),
	('Jack', 'Smith', 58),
    ('Steven', 'Olive', 58),
    ('Paul', 'Tree', 58);

SELECT * FROM employees;