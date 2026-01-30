# Write your MySQL query statement below
SELECT DISTINCT num AS ConsecutiveNums
FROM( 
    SELECT num,
        LAG(num, 1) OVER() AS lag1,
        LAG(num, 2) OVER() AS lag2
    FROM Logs) AS Ls
WHERE num = lag1 and num = lag2
