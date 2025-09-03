# Write your MySQL query statement below
SELECT S.name
FROM SalesPerson AS S
WHERE S.sales_id NOT IN(
    SELECT O.sales_id
    FROM Orders AS O
    WHERE com_id IN(
        SELECT C.com_id
        FROM Company AS C
        WHERE NAME = "RED" 
    )
)