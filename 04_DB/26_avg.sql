-- 26_avg.sql

-- group by 없이 
SELECT AVG(pages) FROM books;

-- group by
SELECT 
    author_fname, 
    author_lname, 
    AVG(pages),
	SUM(pages) / COUNT(*)
FROM
    books
GROUP BY author_fname , author_lname