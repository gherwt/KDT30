-- 16_etc_functions.sql

-- 정해진 구간 안에 원하는 글자를 넣어준다.
SELECT INSERT('Hello Justin', 6, 0, ' There');
SELECT INSERT('Hello Justin', 6, 3, ' There');

-- 왼쪽부터 정해진 수만큼 도출한다.
SELECT LEFT('omglol!', 3);

-- 오른쪽부터 정해진 수만큼 도출한다.
SELECT RIGHT('omglol!', 4);

-- 2개의 결과는 같다.
SELECT LEFT(author_lname, 1) FROM books;
SELECT SUBSTR(author_lname, 1, 1) FROM books;

-- 정해준 수만큼 문자를 반복한다.
SELECT REPEAT('ha', 5);

-- 쓸데없는 공백을 삭제해준다.
SELECT TRIM('           wow             ');
