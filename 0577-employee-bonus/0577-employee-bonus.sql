# Write your MySQL query statement below
SELECT E.name, B.bonus
FROM Employee AS E LEFT OUTER JOIN Bonus AS B ON E.empId = B.empId
WHERE B.bonus is NULL or B.bonus < 1000









-- SELECT e.name, b.bonus
-- FROM Employee AS e LEFT JOIN Bonus AS b ON e.empId = b.empId
-- WHERE b.bonus < 1000 or b.bonus is NULL