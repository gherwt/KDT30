-- practice_09.sql

-- 1번
SELECT COUNT(*) FROM books;

-- 2번
SELECT released_year, COUNT(*) FROM books
GROUP BY released_year ORDER BY released_year;

-- 3번
SELECT SUM(stock_quantity) AS stocks FROM books;

-- 4번
SELECT 
	author_lname, 
	author_fname, 
    AVG(released_year) AS 'avg of released year'
FROM books
GROUP BY author_lname, author_fname;

-- 5번
SELECT CONCAT(author_fname, ' ',author_lname) AS 'full name' , pages AS max_page
FROM books WHERE pages = (SELECT MAX(pages) FROM books);

-- 6번
SELECT 
	released_year AS '출판년도', 
    COUNT(*) '#books', 
    AVG(pages) 'avg pages'
FROM books
GROUP BY released_year
ORDER BY released_year;
