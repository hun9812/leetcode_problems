# Write your MySQL query statement below
SELECT P.product_name, Sum(unit) AS unit
FROM Orders AS O JOIN Products AS P
     ON O.product_id = P.product_id
WHERE O.order_date >= "2020-02-01" and O.order_date <= "2020-02-29"
GROUP BY O.product_id
HAVING SUM(unit) >= 100