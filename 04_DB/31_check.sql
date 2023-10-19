-- 31_check.sql

CREATE TABLE users1(
	username VARCHAR(20) NOT NULL UNIQUE,
    age INT CHECK (age > 0) NOT NULL
    -- check 는 일종의 조건식이라고 할 수 있다.
);

-- Error Code: 3819. Check constraint 'users1_chk_1' is violated. check 조건문을 위반했다.	
INSERT INTO users1(username, age)
VALUES('김철수', '0');

CREATE TABLE palindrome1 (
	word VARCHAR(100) CHECK (word = REVERSE(word))
);

INSERT INTO palindrome1(word) VALUES ('apple');
INSERT INTO palindrome1(word) VALUES ('assa');

-- Name Constraints
CREATE TABLE users2(
	username VARCHAR(20) NOT NULL UNIQUE,
    age INT NOT NULL
    CONSTRAINT age_must_be_postitive CHECK (age >= 0)
);

CREATE TABLE palindrome2 (
	word VARCHAR(100) NOT NULL
    CONSTRAINT word_must_be_palindrome CHECK (word = REVERSE(word))
    );

-- multi columns check
CREATE TABLE companies (
	name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,nameaddressphone
    CONSTRAINT name_and_address_cannot_be_same UNIQUE (name, address)
);

INSERT INTO companies(name, address) 
VALUES ('apple.inc', 'cupertino, CA');

INSERT INTO companies(name, address) 
VALUES ('banana.inc', 'cupertino, CA');

INSERT INTO companies(name, address) 
VALUES ('apple.inc', 'seuol, KR');

CREATE TABLE houses(
	buy_price INT NOT NULL,
    sell_price INT NOT NULL,
    CONSTRAINT sell_gte_buy CHECK(sell_price >= buy_price)
);

INSERT INTO houses(buy_price, sell_price) 
VALUES (10, 20);

INSERT INTO houses(buy_price, sell_price) 
VALUES (20, 10);


