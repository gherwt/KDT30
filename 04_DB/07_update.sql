-- 07_update.sql
-- UPDATE <table> SET <cols>=<val> WHERE <contition>

SELECT 
    *
FROM
    cats;
UPDATE cats SET age = 100 WHERE name = 'Misty';

UPDATE cats SET age = 14 WHERE name = 'Misty';

UPDATE cats SET age = age+1 WHERE name = 'Jackson';
