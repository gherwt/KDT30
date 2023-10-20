-- 12_replace.sql

-- 선택한 문자들을 원하는 문자로 대체할 수 있다.
SELECT REPLACE('HELLO WORLD', 'HELL', '****');
SELECT REPLACE('apple', 'p', 'P');

SELECT REPLACE(title, ' ', '-') AS 'new title' from books;