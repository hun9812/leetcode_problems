# Write your MySQL query statement below
-- SELECT w1.id
-- FROM Weather w1, Weather w2
-- WHERE DATEDIFF(w1.recordDate, w2.recordDate) = 1 AND w1.temperature > w2.temperature

SELECT W1.id
FROM Weather AS W1, Weather AS W2
WHERE DATEDIFF(W1.recordDate, W2.recordDate) = 1 and W1.temperature > W2.temperature