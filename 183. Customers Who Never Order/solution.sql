/*
Find all customers who never order anything.
*/
SELECT name Customers FROM Customers
WHERE id NOT IN (SELECT customerId FROM Orders)
