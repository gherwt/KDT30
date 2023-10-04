-- practice01.sql

-- 1. practive db 생성
CREATE DATABASE practice;

-- practice db로 이동
USE practice;

-- people table 을 생성
CREATE TABLE people(
	first_name VARCHAR(20),
    last_name VARCHAR(20),
    age INT
);

-- people table 조회
DESC people;

-- people table 삭제
DROP TABLE people;
