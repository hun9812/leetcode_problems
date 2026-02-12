# Write your MySQL query statement below
WITH confirm_rate AS(
    SELECT user_id, ROUND(SUM(CASE WHEN action = "confirmed" THEN 1 ELSE 0 END) / COUNT(*) , 2) AS cnt
    FROM Confirmations
    GROUP BY user_id
)

SELECT S.user_id, IFNULL(c.cnt, 0) AS confirmation_rate
FROM Signups AS S LEFT JOIN confirm_rate AS c
ON S.user_id = c.user_id