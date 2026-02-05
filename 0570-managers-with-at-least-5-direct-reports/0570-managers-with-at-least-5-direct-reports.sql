# Write your MySQL query statement below
WITH manager AS(
    SELECT DISTINCT managerId, COUNT(managerId) AS m_num
    FROM Employee
    GROUP BY managerId
)

SELECT E.name
FROM manager m JOIN Employee E
    ON m.managerId = E.id
WHERE m.m_num >=5