# Write your MySQL query statement below
# unbanned users의 cancellation rate구하기. 2013-10-01부터 2013-10-03에 한번이라도 이용

WITH unbanned AS(
    SELECT t.id, t.client_id, t.driver_id, t.status, t.request_at
    FROM
        Trips t JOIN Users u1 ON t.client_id = u1.users_id
                JOIN Users u2 ON t.driver_id = u2.users_id
    WHERE u1.banned != "Yes" and u2.banned != "Yes"
)

SELECT
    request_at AS Day,
    ROUND(1.0 - (SUM(IF(status = "completed",1,0)) / COUNT(*)), 2) AS "Cancellation Rate"
FROM
    unbanned
WHERE
    request_at BETWEEN "2013-10-01" AND "2013-10-03"
GROUP BY
    request_at