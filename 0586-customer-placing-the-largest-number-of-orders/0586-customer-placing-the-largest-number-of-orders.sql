# Write your MySQL query statement belo
SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1



















-- SELECT customer_number
-- FROM Orders
-- GROUP BY customer_number
-- ORDER BY count(customer_number) DESC
-- LIMIT 1;