# Write your MySQL query statement below
WITH first_last AS(
    SELECT student_id, subject,
        FIRST_VALUE(score) OVER(PARTITION BY student_id, subject ORDER BY exam_date ASC) AS first_score,
        FIRST_VALUE(score) OVER(PARTITION BY student_id, subject ORDER BY exam_date DESC) AS latest_score
    FROM Scores
)

SELECT DISTINCT *
FROM first_last
WHERE latest_score > first_score
ORDER BY student_id, subject