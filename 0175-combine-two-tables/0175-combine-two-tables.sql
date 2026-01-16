# Write your MySQL query statement below
-- SELECT Person.firstName, Person.lastName, Address.city, Address.state
-- FROM Person LEFT OUTER JOIN Address ON Person.personId = Address.personId

SELECT P.firstName, P.lastName, A.city, A.state
FROM Person AS P 
LEFT OUTER JOIN Address AS A 
ON P.personId = A.personId 