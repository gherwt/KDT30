-- 14_char_length.sql

-- 글자의 수를 세어준다.
SELECT CHAR_LENGTH('qwer');

SELECT LENGTH('가나다'); -- 영어가 아닌 글자에서 동작이 이상하게 나옴
SELECT CHAR_LENGTH('가나다');

SELECT CHAR_LENGTH(title) AS 'title length', title FROM books;