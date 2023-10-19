-- 18_order_by.sql

-- 정렬 함수, 기본값은 오름차순
SELECT id, author_fname, author_lname from books;

SELECT id, author_fname, author_lname 
FROM books ORDER BY author_fname;

-- 내림차순
SELECT id, author_fname, author_lname 
FROM books ORDER BY author_fname DESC;

SELECT * FROM books ORDER BY stock_quantity DESC;

-- order by가 기준이 되는 컬럼을 숫자로 지정(추천하지 않음)
SELECT id, author_fname, author_lname 
FROM books ORDER BY 2 DESC;

-- 여러 컬럼으로 정렬(칼럼 우선순위가 있다.), order by 순서가 중요하다.
SELECT author_lname, released_year, title FROM books ORDER BY author_lname, released_year;
SELECT author_lname, released_year, title FROM books ORDER BY released_year, author_lname;

SELECT author_lname, released_year, title FROM books ORDER BY author_lname, released_year DESC;
SELECT author_lname, released_year, title FROM books ORDER BY author_lname DESC, released_year DESC;

-- 가상의 컬럼으로도 정렬 가능하다.
SELECT CONCAT(author_fname, ' ', author_lname) AS author
FROM books ORDER BY author;