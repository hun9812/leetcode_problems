# Write your MySQL query statement below
SELECT P.product_id, P.product_name
FROM Product AS P JOIN Sales AS S ON p.product_id = s.product_id
GROUP BY S.product_id
HAVING MIN(s.sale_date) >= '2019-01-01' 
   AND MAX(s.sale_date) <= '2019-03-31';