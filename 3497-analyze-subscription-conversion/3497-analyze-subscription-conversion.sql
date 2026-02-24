# Write your MySQL query statement below
WITH paid_user AS (
    SELECT DISTINCT user_id
    FROM UserActivity
    WHERE activity_type = "paid"
)

SELECT user_id,
    ROUND(AVG(IF(activity_type = "free_trial", activity_duration, NULL)), 2) AS trial_avg_duration,
    ROUND(AVG(IF(activity_type = "paid", activity_duration, NULL)), 2) AS paid_avg_duration
FROM UserActivity
WHERE user_id in (SELECT * FROM paid_user)
GROUP BY user_id