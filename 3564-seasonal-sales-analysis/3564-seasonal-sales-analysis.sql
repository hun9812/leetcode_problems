# Write your MySQL query statement below
# 12 1 2 겨울, 3 4 5 spring,...
WITH each_season AS(
    SELECT p.category,
           CASE WHEN month(sale_date) between 3 and 5 THEN "Spring"
                WHEN month(sale_date) between 6 and 8 THEN "Summer"
                WHEN month(sale_date) between 9 and 11 THEN "Fall"
                ELSE "Winter" END AS season,
            SUM(s.quantity) AS total_quantity, SUM(s.quantity*s.price) AS total_revenue
    FROM sales s JOIN products p ON s.product_id = p.product_id
    GROUP BY season, p.category
    ORDER BY total_quantity DESC, total_revenue DESC
)

SELECT season, category, total_quantity, total_revenue
FROM each_season
GROUP BY season
ORDER BY season