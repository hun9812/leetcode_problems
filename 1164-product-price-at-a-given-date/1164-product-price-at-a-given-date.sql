# Write your MySQL query statement below
WITH last_date AS (
    SELECT *
    FROM(
        SELECT product_id, change_date,
            ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY change_date DESC) as rnk
        FROM Products
        WHERE change_date <= "2019-08-16"
    ) AS e
    WHERE rnk = 1
)
SELECT R.product_id, IFNULL(K.price, 10) AS price
FROM (SELECT DISTINCT product_id FROM Products) AS R LEFT JOIN (
    SELECT P.product_id, P.new_price AS price
    FROM Products AS P JOIN last_date AS L
         ON P.product_id = L.product_id and P.change_date = L.change_date) AS K
    ON R.product_id = K.product_id