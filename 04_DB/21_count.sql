-- 21_count.sql

-- row의 갯수를 세는 것임
-- 어떤 colunm 을 사용해도 같은 갯수가 나온다.
SELECT COUNT(*) FROM books;
SELECT COUNT(id) FROM books;

-- 소속된 레코드의 숫자를 세준다.
SELECT COUNT(DISTINCT author_lname) FROM books;
SELECT COUNT(*) FROM books WHERE title LIKE '%the%';
SELECT COUNT(title) FROM books WHERE title LIKE '%the%';

-- Error(aggregated - non aggregated 는 동시 조회 불가능) sql mode full group by 에 의해서 2개를 동시에 보여줄 수는 없다.(incompatible)
SELECT titile, COUNT(*) FROM books WHERE title LIKE '%the%';