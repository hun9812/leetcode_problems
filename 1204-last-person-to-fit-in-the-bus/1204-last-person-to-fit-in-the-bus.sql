# Write your MySQL query statement below
WITH weight_sum AS (
    SELECT person_name, turn,
        SUM(weight) OVER(ORDER BY turn ASC) AS cur_weight
    FROM Queue
    ORDER BY turn ASC
)

SELECT person_name
FROM weight_sum
WHERE cur_weight <= 1000
ORDER BY turn DESC
LIMIT 1