# Write your MySQL query statement below
WITH all_pair AS(
    SELECT P1.user_id, P1.product_id as product1_id, P2.product_id as product2_id
    FROM ProductPurchases P1 JOIN ProductPurchases P2
        ON P1.user_id = P2.user_id AND P1.product_id < P2.product_id
)

SELECT t.product1_id, t.product2_id, I1.category AS product1_category, I2.category AS product2_category,
       t.customer_count
FROM (SELECT product1_id, product2_id, COUNT(*) AS customer_count 
      FROM all_pair
      GROUP BY product1_id, product2_id
      HAVING COUNT(*) >= 3) AS t
      LEFT JOIN ProductInfo I1 ON t.product1_id = I1.product_id
      LEFT JOIN ProductInfo I2 ON t.product2_id = I2.product_id
ORDER BY t.customer_count DESC, t.product1_id ASC, t.product2_id ASC