-- 22_group_by.sql

SELECT author_lname FROM books;

-- 결과는 비슷하지만 실제로는 다르다.
-- 겉으로 보이기에는 같지만 group by 는 group by 의 기준으로 data들이 묶여있는 것이라고 보면 된다.
-- excel 의 피벗테이블과 유사하다.
SELECT author_lname FROM books GROUP BY author_lname;
SELECT DISTINCT author_lname FROM books;

-- group 되어져있는 레코드를 세어준다.
SELECT 
    author_lname, COUNT(*) AS COUNTER
FROM
    books
GROUP BY author_lname
-- 작가별 책이 많은 순으로 정렬
ORDER BY COUNTER DESC;

-- 2개를 기준으로 grouping 해서 정렬 가능
SELECT author_lname, author_fname, COUNT(*) FROM books
GROUP BY author_lname, author_fname; 

-- 2개 열을 합쳐서 새로운 열을 만들고 기준으로 사용
SELECT CONCAT(author_lname, ' ', author_fname) AS fullname, COUNT(*)
FROM books GROUP BY fullname;

