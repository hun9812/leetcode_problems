# Write your MySQL query statement below
SELECT Users.name AS NAME, T_balance.BALANCE
FROM Users JOIN (
    SELECT account, SUM(amount) AS BALANCE
    FROM Transactions
    GROUP BY account) AS T_balance ON T_balance.account = Users.account
WHERE T_balance.BALANCE > 10000