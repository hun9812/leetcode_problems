# Write your MySQL query statement below
WITH rank_rating AS (
    SELECT employee_id, rating,
           LAG(rating, 1) OVER (PARTITION BY employee_id ORDER BY review_date ASC) AS rating_b1,
           LAG(rating, 2) OVER (PARTITION BY employee_id ORDER BY review_date ASC) AS rating_b2,
           ROW_NUMBER() OVER (PARTITION BY employee_id ORDER BY review_date DESC) AS row_rank
    FROM performance_reviews
)
SELECT r.employee_id, name, (rating - rating_b2) AS improvement_score
FROM rank_rating r JOIN employees e ON r.employee_id = e.employee_id
WHERE row_rank = 1 and rating > rating_b1 and rating_b1 > rating_b2 
ORDER BY improvement_score DESC, name ASC