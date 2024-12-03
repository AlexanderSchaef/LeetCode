/*
- [x] Select the second highest salary
        Achieved by narrowing the field to ignore the highest salary, and looking for the highest salary
- [x] Rename the display column name for the select statement
*/

SELECT DISTINCT max(salary) SecondHighestSalary FROM Employee
WHERE salary NOT IN (SELECT max(salary) FROM Employee);
