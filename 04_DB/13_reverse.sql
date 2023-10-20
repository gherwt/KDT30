-- 13_reverse.sql

-- 글의 순서를 뒤집어준다. (index 값을 뒤집어준다.)
SELECT REVERSE('apple');

SELECT REVERSE(author_fname) AS strange_name FROM books;