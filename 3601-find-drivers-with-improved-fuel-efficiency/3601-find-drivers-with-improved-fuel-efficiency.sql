# Write your MySQL query statement below
WITH half_year AS(
    SELECT t.driver_id, d.driver_name, 
        AVG((t.distance_km)/(t.fuel_consumed)) AS efficiency,
        CASE WHEN MONTH(t.trip_date) <= 6 THEN "first_half"
        ELSE "second_half" END AS check_half
    FROM trips t JOIN drivers d
        ON t.driver_id = d.driver_id
    GROUP BY driver_id, check_half
)

SELECT h1.driver_id, h1.driver_name, ROUND(h1.efficiency,2) AS first_half_avg,
    ROUND(h2.efficiency ,2) AS second_half_avg, ROUND(h2.efficiency - h1.efficiency, 2) AS efficiency_improvement
FROM half_year h1 JOIN half_year h2 ON h1.driver_id = h2.driver_id
WHERE h1.check_half = "first_half" and h2.check_half = "second_half"
    and h1.efficiency < h2.efficiency
ORDER BY efficiency_improvement DESC, h1.driver_name ASC