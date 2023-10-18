-- 23_min_max.sql

-- group by 없이 사용
-- 나타나는 값은 1개이지만 집계되어서 나오기 때문에 몇개의 값이 있을지 모른다.
SELECT MIN(released_year) FROM books;

-- 가장 큰 page 
SELECT MAX(pages) FROM books;

-- abc 순도 나타낼 수 있다.
SELECt MIN(author_lname), MAX(author_lname) FROM books;

-- group by 함께 사용
-- 작가별 출판한 책 수, 가장 오래된 책 출판년도, 가장 최근 책 출판년도
SELECT -- 1) aggregated 2) group col
	author_lname AS '성', 
    author_fname AS '이름',
    COUNT(title) AS '책 수',
    MIN(released_year) AS '최고', 
    MAX(released_year) AS '최신'
FROM books
GROUP BY author_lname, author_fname;