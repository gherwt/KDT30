-- 04_default.sql

drop table dogs3;

CREATE TABLE dogs3 (
	name VARCHAR(20) DEFAULT 'No Name',
    age INT DEFAULT 0
);

INSERT INTO dogs3 () VALUES ();

SELECT * FROM dogs3;

INSERT INTO dogs3 (name) VALUES (NULL);

CREATE TABLE dogs4 (
	name VARCHAR(20) NOT NULL DEFAULT 'No Name',
    age INT NOT NULL DEFAULT 0
);

-- Error 발생
INSERT INTO dogs4 (name) VALUES(NULL);