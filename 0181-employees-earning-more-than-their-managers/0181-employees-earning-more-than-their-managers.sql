# Write your MySQL query statement below
-- SELECT e.name as Employee
-- FROM Employee as e, Employee as m
-- WHERE e.managerId = m.id and e.salary > m.salary

SELECT E.name AS Employee
FROM Employee AS E
JOIN Employee AS M ON E.managerId = M.id
WHERE E.salary > M.salary