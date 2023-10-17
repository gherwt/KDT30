-- 17_distinct.sql(uniq)

-- 함수가 아니다. 중복값을 제거해준다.
SELECT author_lname FROM books;
SELECT DISTINCT author_lname FROM books;

SELECT released_year FROM books;
SELECT DISTINCT released_year FROM books;

-- 풀 네임에서 중복을 없이 보려면
SELECT CONCAT(author_fname, ' ', author_lname) AS full_name from books;

SELECT DISTINCT author_fname, author_lname from books;
-- 칼럼이 모두 종복되는 경우가 없으므로 전체 레코드가 조회된다.
SELECT DISTINCT author_fname, author_lname, released_year from books;