-- practice_08.sql

-- 1번
SELECT title FROM books AS title WHERE title LIKE '%stories%';

-- 2번
SELECT title, pages FROM books ORDER BY pages DESC Limit 1;

-- 3번
SELECT CONCAT(title, '-', released_year) AS summary FROM books ORDER BY released_year DESC limit 3;

-- released_year 가 내림차순 정렬된 결과에서 3개만 limit 걸기로 문제가 나오지 않는다.

-- 4번
SELECT title, author_lname FROM books WHERE author_lname LIKE '% %';

-- 5번
SELECT title, released_year, stock_quantity FROM books ORDER BY stock_quantity limit 3;

-- 6번
SELECT title, author_lname FROM books ORDER BY author_lname, title;

-- 7번
SELECT DISTINCT UPPER(CONCAT(author_fname, ' ', author_lname, '!!!')) AS shoutout
FROM books ORDER BY shoutout;
