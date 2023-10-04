-- 03_NULL.sql

USE pet_shop;

INSERT INTO dogs1 (name, breed)
VALUES ('멍뭉이','시고르');

-- null yes 는 어떤 값을 안 받을 수 있다는 것을 의미한다.

INSERT INTO dogs1 () VALUES ();

-- New Table

CREATE TABLE dogs3 (
	name VARCHAR(20) NOT NULL,
    age INT NOT NULL
);

DESC dogs2;

INSERT INTO dogs2 (name) VALUES ('doggy');
INSERT INTO dogs2 (name, age) VALUES ('doggy', 3);

select * from dog2;