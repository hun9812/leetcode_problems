# Write your MySQL query statement below
SELECT name
FROM SalesPerson
WHERE sales_id NOT IN(
SELECT DISTINCT sales_id
FROM Orders AS O JOIN Company AS C ON O.com_id = C.com_id
WHERE C.name = "RED"
)















-- SCELECT S.name
-- FROM SalesPerson AS S
-- WHERE S.sales_id NOT IN(
--     SELECT O.sales_id
--     FROM Orders AS O
--     WHERE com_id IN(
--         SELECT C.com_id
--         FROM Company AS 
--         WHERE NAME = "RED" 
--     )
-- )