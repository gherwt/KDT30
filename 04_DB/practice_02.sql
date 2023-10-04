-- practice02.sql

-- 1. practice db 사용
USE practice;

-- 2. 테이블 people 생성
-- 3. first_name varchar(20)
-- 4. first_name varchar(20)
-- 5. age INT

CREATE TABLE people(
	first_name varchar(20),
	last_name varchar(20),
    age INT);

-- 6. 테이블 확인
DESC people;

-- 7. 데이터 입력 3명 넣기

INSERT INTO people(first_name, last_name, age)
values
	('상민', '이', 27),
	('찬연', '변', 26),
	('용','송',27);

SELECT * FROM people;