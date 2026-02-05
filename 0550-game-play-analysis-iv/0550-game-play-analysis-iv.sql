# Write your MySQL query statement below
WITH earlist AS (
    SELECT player_id, MIN(event_date) AS first
    FROM Activity
    GROUP BY player_id
)

SELECT ROUND(COUNT(A.event_date) / COUNT(e.player_id), 2) AS fraction
FROM earlist e LEFT JOIN Activity A
    ON e.player_id = A.player_id and DATEDIFF(A.event_date, e.first) = 1