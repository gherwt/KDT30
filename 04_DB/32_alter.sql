-- 32_alter.sql

-- CRUD

-- ADD Column
ALTER TABLE companies
ADD COLUMN phone VARCHAR(15);

-- 논리적 오류
-- default 값을 준 적이 없지만 0이 입력되었다.
ALTER TABLE companies
ADD COLUMN employee_count INT NOT NULL;

ALTER TABLE companies
ADD COLUMN income INT NOT NULL DEFAULT 1;

-- Delete Column
ALTER TABLE companies
DROP COLUMN phone;

-- Rename Table
RENAME TABLE companies TO suppliers;
ALTER TABLE suppliers RENAME TO companies;

-- Rename Column
ALTER TABLE companies
RENAME COLUMN name TO company_name;

-- Update Column 
-- data type 변경 시에 주의하자.
ALTER TABLE companies
MODIFY company_name VARCHAR(100) DEFAULT '???';

-- Rename & update Column
ALTER TABLE companies
CHANGE company_name name VARCHAR(255) DEFAULT '???' NOT NULL;

-- Update Constraints
ALTER TABLE houses
ADD CONSTRAINT positive_buy_price CHECK (buy_price >= 0);

ALTER TABLE houses DROP CONSTRAINT positive_buy_price;
