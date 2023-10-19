-- 06_read.sql

USE pet_shop;

CREATE TABLE cats (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    breed VARCHAR(100),
    age INT
);

INSERT INTO cats(name, breed, age) 
VALUES ('Ringo', 'Tabby', 4),
       ('Cindy', 'Maine Coon', 10),
       ('Dumbledore', 'Maine Coon', 11),
       ('Egg', 'Persian', 4),
       ('Misty', 'Tabby', 13),
       ('George Michael', 'Ragdoll', 9),
       ('Jackson', 'Sphynx', 7);


-- READ : select col from table;
SELECT * FROM cats;
SELECT name FROM cats;
SELECT age, breed FROM cats;

-- 단일 조회 , where을 사용한 조건식 where 이 if 구문이라고 보면 된다.
SELECT * FROM cats WHERE age=4
SELECT name FROM cats WHERE age=4;
SELECT age, breed FROM cats WHERE age=4;

-- 대소문자에 대해서 유연하게 검색해준다. Case Insensitive 하다
SELECT * FROM cats WHERE name = 'egg';
SELECT * FROM cats WHERE name = 'eGg';

-- 조회하는 col 명을 바꿔주는 as 구문 
SELECT name AS '이름' FROM cats;
SELECT name AS '이름', breed AS '종' FROM cats;

