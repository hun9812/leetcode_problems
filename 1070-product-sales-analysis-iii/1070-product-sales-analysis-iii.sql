# Write your MySQL query statement below
WITH earlist AS(
    SELECT product_id, MIN(year) AS year
    FROM Sales
    GROUP BY product_id
)

SELECT S.product_id, S.year AS first_year, S.quantity, S.price
FROM Sales AS S, earlist AS E 
WHERE S.product_id = E.product_id AND
      S.year = E.year