# Write your MySQL query statement below
(select employee_id from Employees except select employee_id from Salaries)
union
(select employee_id from Salaries except select employee_id from Employees)
order by employee_id asc