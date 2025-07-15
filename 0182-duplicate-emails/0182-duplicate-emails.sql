# Write your MySQL query statement below
SELECT distinct P1.email as Email
From Person as P1, Person as P2
WHERE P1.id != P2.id and P1.email = P2.email