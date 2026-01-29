# Write your MySQL query statement below
select *
from products
where REGEXP_LIKE(description, " SN[0-9]{4}\\-[0-9]{4} ", 'c') 
or REGEXP_LIKE(description, " SN[0-9]{4}\\-[0-9]{4}$", 'c')
or REGEXP_LIKE(description, "^SN[0-9]{4}\\-[0-9]{4} ", 'c')
or REGEXP_LIKE(description, "^SN[0-9]{4}\\-[0-9]{4}$", 'c')
order by product_id