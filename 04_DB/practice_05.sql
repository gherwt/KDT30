-- practice_05

-- UPDATE <table> SET <cols>=<val> WHERE <contition>

UPDATE cats 
SET 
    name = 'jack'
WHERE
    name = 'jackson';

UPDATE cats 
SET 
    breed = 'British Shorthair'
WHERE
    breed = 'Ringo';

UPDATE cats 
SET 
    age = 12
WHERE
    breed = 'Maine Coon';
    
SELECT 
    *
FROM
    cats;
