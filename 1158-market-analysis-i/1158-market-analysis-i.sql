# Write your MySQL query statement below
WITH bought AS(
    SELECT buyer_id, COUNT(*) AS ordered
    FROM Orders
    WHERE order_date >= '2019-01-01' and order_date <= '2019-12-31'
    GROUP BY buyer_id
)

SELECT U.user_id AS buyer_id, U.join_date, IFNULL(bought.ordered, 0) AS orders_in_2019
FROM Users AS U LEFT JOIN bought
                ON U.user_id = bought.buyer_id
