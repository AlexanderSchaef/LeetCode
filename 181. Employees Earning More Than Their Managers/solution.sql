-- Find employees who earn more than their managers
SELECT e.name Employee FROM employee e
JOIN employee m ON e.managerId = m.id
WHERE m.salary < e.salary;
