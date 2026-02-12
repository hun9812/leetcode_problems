# Write your MySQL query statement below
SELECT s.stock_name,  s.price-b.price AS capital_gain_loss
FROM (
    SELECT stock_name, SUM(price) AS price
    FROM Stocks
    WHERE operation = "Sell"
    GROUP BY stock_name
)AS s JOIN (
    SELECT stock_name, SUM(price) AS price
    FROM Stocks
    WHERE operation = "Buy"
    GROUP BY stock_name
) AS b
ON s.stock_name = b.stock_name