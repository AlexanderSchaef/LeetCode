/*
Write a solution to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL.
*/

SELECT DISTINCT p1.email Email 
FROM Person p1
WHERE (SELECT COUNT(p2.email) FROM Person p2 WHERE p2.email=p1.email) > 1;
