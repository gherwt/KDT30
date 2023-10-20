-- 30_unique.sql

CREATE DATABASE constraints_alter;

USE constraints_alter;

CREATE TABLE contacts (
	name VARCHAR(100) NOT NULL,
  phone VARCHAR(15) NOT NULL UNIQUE
  -- 제약 조건임
);

INSERT INTO contacts (name, phone)
VALUES ('김김김', '01012345667');

INSERT INTO contacts (name, phone)
VALUES ('박박박', '01012345667');