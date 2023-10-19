-- 24_subquery.sql

-- aggregated 와 non aggregated 는 함께 조회 불가능
SELECT MAX(pages), title FROM books;

-- 중복된 값을 도출하지 않는다.
SELECT title, pages FROM books
ORDER BY pages DESC LIMIT 1;

-- 2줄 커리
SELECT MAX(pages) FROM books;
SELECT title, pages FROM books WHERE pages = 634;

-- subquery 로 1줄로 처리
SELECT title, pages FROM books 
WHERE pages = (SELECT MAX(pages) FROM books);

-- 가장 오래된 책
SELECT MIN(released_year) FROM books;
SELECT title, released_year FROM books WHERE released_year =1945;

SELECT title, released_year FROM books WHERE released_year =(SELECT MIN(released_year) FROM books);
