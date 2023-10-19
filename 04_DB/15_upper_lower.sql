-- 15_upper_lower.sql

-- 글자를 대문자로 바꿔준다.
SELECT UPPER('hello');

-- 글자를 소문자로 바꿔준다.
SELECT LOWER('WORLD');

SELECT UPPER(title) AS upper_title FROM books;
SELECT LOWER(title) AS upper_title FROM books;

-- 'I LOVE <BOOK_TITLE>!!!'
-- concat 함께 사용할 수 있다.
SELECT UPPER(CONCAT('i love ', title, '!!!')) AS love_book_title FROM books;
SELECT CONCAT('I LOVE ', UPPER(title), '!!!') AS love_book_title FROM books;