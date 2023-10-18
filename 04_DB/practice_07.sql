-- practice07.sqlbooks

-- 1번 문제
SELECT REPLACE( title, ' ', '->') AS 'title' FROM books;

-- 2번문제
SELECT author_lname AS forwards, REVERSE(author_lname) AS 'backwards' FROM books;

-- 3번문제
SELECT UPPER(CONCAT(author_fname, ' ',author_lname))AS 'full name in caps' FROM books; 

SELECT UPPER(CONCAT_WS(' ', author_fname, author_lname))AS 'full name in caps' FROM books; 

-- 4번문제
SELECT CONCAT(title, ' was released in ', released_year) AS 'summary' FROM books;

-- 5번문제
SELECT title,
	CHAR_LENGTH(title) AS 'character count' FROM books;
    
-- 6번 문제
SELECT 
    CONCAT(SUBSTR(title, 1, 10), '...') AS 'short title',
    CONCAT(author_lname, ',', author_fname) AS 'author',
    CONCAT(stock_quantity, ' in stock') AS 'quantity'
FROM
    books;
