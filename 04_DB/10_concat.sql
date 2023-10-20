-- 10_concat.sql

-- 문자들을 합쳐준다.
SELECT CONCAT('s', 'q', 'l');

-- table 에서 자료를 뽑아와서 합쳐줄 수 도 있다.
SELECT CONCAT(author_fname, '!!!') FROM books;

SELECT CONCAT(author_fname, ' ', author_lname) FROM books;

SELECT CONCAT(author_fname, ' ', author_lname) AS full_name FROM books;

SELECT CONCAT('!', 's', 'q', 'l');
-- concat이 그냥 문자들을 합쳐주는 것이라면 concat_ws 는 사이에 원하는 문자를 넣어주는 것이라고 보면 된다.
SELECT CONCAT_WS('!', 's', 'q', 'l');

SELECT CONCAT_WS('-', title, author_fname, author_lname) AS summary From books;