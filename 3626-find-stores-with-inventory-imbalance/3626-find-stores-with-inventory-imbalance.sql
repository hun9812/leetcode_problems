# Write your MySQL query statement below
WITH rank_data AS(
    SELECT store_id,product_name, quantity, price,
           ROW_NUMBER() OVER(PARTITION BY store_id ORDER BY price ASC) AS cheap,
           ROW_NUMBER() OVER(PARTITION BY store_id ORDER BY price DESC) AS expensive
    FROM inventory
    WHERE store_id in (SELECT store_id FROM inventory GROUP BY store_id HAVING COUNT(*)>=3)
)

SELECT r.store_id, s.store_name, s.location, most_exp_product, cheapest_product, imbalance_ratio
FROM (SELECT r1.store_id, r1.product_name AS most_exp_product, r2.product_name AS cheapest_product,
             ROUND((r2.quantity/r1.quantity),2) AS imbalance_ratio
     FROM rank_data r1 JOIN rank_data r2
          ON r1.store_id = r2.store_id
     WHERE r1.expensive = 1 and r2.cheap = 1 and
             r1.quantity < r2.quantity) AS r
     JOIN stores s
     ON r.store_id = s.store_id
ORDER BY imbalance_ratio DESC, store_name ASC