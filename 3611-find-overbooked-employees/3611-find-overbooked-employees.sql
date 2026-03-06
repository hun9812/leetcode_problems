# Write your MySQL query statement below
WITH heavy_meeting AS(
    SELECT YEARWEEK(m.meeting_date, 1) AS id, m.employee_id, e.employee_name, e.department
    FROM meetings m JOIN employees e
         ON m.employee_id = e.employee_id
    GROUP BY m.employee_id, YEARWEEK(m.meeting_date, 1)
    HAVING SUM(duration_hours) >= 20
)

SELECT employee_id, employee_name, department, COUNT(employee_id) AS meeting_heavy_weeks
FROM heavy_meeting
GROUP BY employee_id
HAVING COUNT(*) >= 2
ORDER BY meeting_heavy_weeks DESC, employee_name ASC