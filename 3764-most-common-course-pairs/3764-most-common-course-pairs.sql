# Write your MySQL query statement below
WITH top_student AS(
    SELECT
        user_id
    FROM
        course_completions
    GROUP BY
        user_id
    HAVING
        COUNT(*) >= 5 and
        AVG(course_rating) >= 4
),
course_lag AS(
    SELECT
        user_id, course_name AS second_course,
        LAG(course_name, 1) OVER (PARTITION BY user_id ORDER BY completion_date) AS first_course
    FROM
        course_completions
    WHERE
        user_id IN (SELECT user_id FROM top_student)
)


SELECT
    first_course, second_course,
    COUNT(*) AS transition_count
FROM 
    course_lag
WHERE
    first_course is not NULL
GROUP BY
    first_course, second_course
ORDER BY
    transition_count DESC, first_course ASC, second_course ASC