-- 25_sum.sql

-- group_by 가 없으면 전체의 자동 합계
SELECT SUM(pages), SUM(stock_quantity) FROM books;

-- 작가별 재고 수의 총 합
SELECT 
    author_fname, 
    author_lname, 
    SUM(stock_quantity)
FROM
    books
GROUP BY author_lname , author_fname;