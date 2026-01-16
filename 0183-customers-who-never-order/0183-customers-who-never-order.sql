# Write you r MySQL query statement below
-- SELECT name as Customers
-- FROM Customers
-- WHERE NOT EXISTS (
--     SELECT customerId
--     FROM Orders
--     WHERE Orders.customerId = Customers.id 
-- )

-- SELECT C.name AS Customers
-- FROM Customers AS C
-- LEFT OUTER JOIN Orders AS O
-- ON C.id = O.customerId
-- GROUP BY C.id
-- HAVING COUNT(customerId) = 0

SELECT name AS Customers
FROM Customers C
WHERE NOT EXISTS (
    SELECT 1 
    FROM Orders O 
    WHERE O.customerId = C.id
);