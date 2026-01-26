# Write your MySQL query statement below
SELECT *
FROM Users
WHERE mail COLLATE utf8_bin REGEXP '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\\.com$';