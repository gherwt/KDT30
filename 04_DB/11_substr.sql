-- 11_substr

-- SELECT SUBSTR(<str>, <start>, <length>)
-- SELECT SUBSTR(<str>, <start>)

-- 선택한 문자에서 시작 지점, 길이를 선택하여 뽑아낸 후 이를 return 해준다.
SELECT SUBSTR('HELLO, WORLD', 1, 4);
-- HELL
SELECT SUBSTR('HELLO, WORLD', 2, 4);
-- ELLO

SELECT SUBSTR('HELLO, WORLD', 1);
-- HELLO, WORLD
SELECT SUBSTR('HELLO, WORLD', 7);
-- WORLD
SELECT SUBSTR('HELLO, WORLD', 8);
-- WORLD

-- - index도 사용가능하다.
SELECT SUBSTR('HELLO, WORLD', -5);
-- WORLD
SELECT SUBSTR('HELLO, WORLD', -5, 2);
-- WO

-- concat 과도 연동해서 사용가능하다.
SELECT 
    CONCAT(SUBSTR(title, 1, 10), '...') AS 'short title',
    CONCAT(SUBSTR(author_lname, 1, 1),
            '.',
            author_fname) AS 'name'
FROM
    books;
