# Write your MySQL query statement below
# 지금 active subscription이 있고(last event 가 cancel이 아님)
# 최소 한번의 downgrade가 있고
# 현재 revenue가 본인 최고점의 50% 미만이고 60일이상 구독
WITH filter AS(
    SELECT
        *,
        ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY event_date DESC) AS recent_date,
        MAX(monthly_amount) OVER(PARTITION BY user_id) AS max_amount,
        SUM(IF(event_type = "downgrade", 1, 0)) OVER(PARTITION BY user_id) AS down_count,
        DATEDIFF(MAX(event_date) OVER(PARTITION BY user_id), 
                 MIN(event_date) OVER(PARTITION BY user_id)) AS date_count
    FROM subscription_events
)

SELECT user_id, plan_name AS current_plan, monthly_amount AS current_monthly_amount,
    max_amount AS max_historical_amount,
    date_count AS days_as_subscriber
FROM filter
WHERE
    recent_date = 1 and
    monthly_amount < (max_amount*0.5) and
    event_type != "cancel" and
    date_count >= 60 and
    down_count > 0
ORDER BY days_as_subscriber DESC, user_id ASC