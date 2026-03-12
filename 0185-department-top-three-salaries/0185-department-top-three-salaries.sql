# Write your MySQL query statement below
# DENSE_RANK
WITH rank_salary AS(
    SELECT
        e.name AS Employee,
        e.salary AS Salary,
        d.name AS Department,
        d.id AS d_id,
        DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY e.salary DESC) AS salary_rank
    FROM
        Employee e JOIN Department d
        ON  e.departmentId = d.id
)

SELECT Department, Employee, Salary
FROM rank_salary
WHERE salary_rank <= 3