-- 07_update.sql
-- UPDATE <table> SET <cols>=<val> WHERE <contition>
-- 파일을 수정해준다.edit

SELECT 
    *
FROM
    cats;
UPDATE cats SET age = 100 WHERE name = 'Misty';

UPDATE cats SET age = 14 WHERE name = 'Misty';

UPDATE cats SET age = age+1 WHERE name = 'Jackson';
