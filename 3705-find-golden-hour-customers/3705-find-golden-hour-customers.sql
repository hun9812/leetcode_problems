# Write your MySQL query statement below
WITH peak_hour_order AS(
    SELECT customer_id, COUNT(*) AS peak_count
    FROM restaurant_orders
    WHERE (HOUR(order_timestamp) BETWEEN 11 AND 13) OR (HOUR(order_timestamp) BETWEEN 18 AND 20)
    GROUP BY customer_id
)

SELECT
    s.customer_id,
    COUNT(*) AS total_orders,
    s.peak_hour_percentage,
    ROUND(AVG(order_rating),2) AS average_rating
FROM restaurant_orders c 
    RIGHT JOIN (
        SELECT
            a.customer_id,
            ROUND(p.peak_count * 100.0 /a.whole_count, 0) AS peak_hour_percentage
        FROM (SELECT customer_id, COUNT(*) AS whole_count FROM restaurant_orders GROUP BY customer_id) AS a        JOIN peak_hour_order p ON a.customer_id = p.customer_id
        WHERE (p.peak_count * 1.0 / a.whole_count) >= 0.6
) AS s ON c.customer_id = s.customer_id
GROUP BY
    s.customer_id,
    s.peak_hour_percentage
HAVING 
    COUNT(*) >= 3 AND
    (COUNT(order_rating) * 1.0 / COUNT(*)) >= 0.5 AND
    ROUND(AVG(order_rating),2) >= 4
ORDER BY average_rating DESC, s.customer_id DESC