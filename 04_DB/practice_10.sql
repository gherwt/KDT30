-- practice_10.sql

-- 1
SELECT COUNT(*) FROM books WHERE released_year < 1980;

-- 2
SELECT * FROM books 
WHERE  author_lname = 'Eggers' OR author_lname = 'Chabon';

SELECT * FROM books WHERE author_lname IN('Eggers', 'Chabon');

-- 3
SELECT * FROM books 
WHERE  author_lname = 'Lahiri' AND released_year > 2000;

-- 4
SELECT title, pages FROM books 
WHERE pages BETWEEN 100 AND 200;

-- 5
SELECT title, author_lname FROM books 
WHERE author_lname LIKE 'c%' OR  author_lname LIKE 's%';

-- 6
SELECT title, stock_quantity, 
	CASE
		WHEN title LIKE '%stories%' THEN 'A'
		WHEN title LIKE '%kids%' 
        or title LIKE '%heartbreaking%' THEN 'B'
		ELSE 'C'
	END AS 'type'
FROM books;

