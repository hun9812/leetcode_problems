# Write your MySQL query statement below
SELECT visited_on,
       sum_6.amount,
       ROUND(sum_6.amount / 7, 2) AS average_amount
FROM (
    SELECT visited_on,
           SUM(amount) OVER (ORDER BY visited_on ASC ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount
           #SUM(cnt) OVER (ORDER BY visited_on ASC ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS cnt
    FROM (
        SELECT visited_on, SUM(amount) AS amount, COUNT(*) AS cnt
        FROM Customer
        GROUP BY visited_on
        ORDER BY visited_on ASC
    ) AS temp
) AS sum_6
WHERE visited_on >= (SELECT MIN(visited_on) FROM Customer) + INTERVAL 6 DAY