# Write your MySQL query statement below
with cte as
(select *,dense_rank() over (partition by departmentId order by salary desc ) as rnk
from
Employee
)

select t2.name as Department,t1.name as Employee,t1.salary as Salary
from cte t1
left join Department t2
on t1.departmentId=t2.id
where rnk in (1,2,3)