# Write your MySQL query statement below
WITH consec AS(
    SELECT *,
        LAG(people, 1) OVER(ORDER BY visit_date ASC) AS lag_1,
        LAG(people, 2) OVER(ORDER BY visit_date ASC) AS lag_2,
        LEAD(people, 1) OVER(ORDER BY visit_date ASC) AS lead_1,
        LEAD(people, 2) OVER(ORDER BY visit_date ASC) AS lead_2
    FROM Stadium
)

SELECT id, visit_date, people 
FROM
    consec
WHERE
    people >= 100 and (
    (lag_1 >= 100 and lag_2 >= 100) or
    (lag_1 >= 100 and lead_1 >=100) or
    (lead_1 >=100 and lead_2 >=100)
    )
ORDER BY
    visit_date ASC