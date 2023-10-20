-- 28_operator2

-- AND
SELECT title, author_lname, released_year FROM books
WHERE
	released_year > 2010
    AND
    author_lname = 'Eggers';
    
SELECT title, author_lname, released_year FROM books
WHERE
	released_year > 2010
    AND
    author_lname = 'Eggers'
    AND
    title LIKE '%novel%';
    
SELECT title, author_lname, released_year FROM books
WHERE
	released_year >= 2000
    AND
    released_year % 2 =1;
    
    
-- OR

SELECT title, author_lname, released_year FROM books
WHERE
	released_year > 2010
    OR
	author_lname = 'Eggers';

SELECT title, pages FROM books
WHERE
	pages <200
    OR
	title LIKE '%novel%';

-- BETWEEN
SELECT title, released_year FROM books
WHERE
	released_year >= 2094
    AND
    released_year <= 2015;

SELECT title, released_year FROM books
WHERE released_year BETWEEN 2004 AND 2015;

SELECT title, pages FROM books
WHERE pages NOT BETWEEN 200 AND 300;

SELECT title, pages FROM books
WHERE pages < 200 or pages > 300;

-- In
SELECT title, pages FROM books
WHERE author_lname = 'Caver' OR author_lname = 'Lahiri' OR author_lname = 'Smith';

SELECT title, pages FROM books
WHERE author_lname IN ('Caver', 'Lahiri', 'Smith');

SELECT title, pages FROM books
WHERE author_lname NOT IN ('Caver', 'Lahiri', 'Smith');
