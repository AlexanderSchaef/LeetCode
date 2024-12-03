/*
Question states null values for Address fields if there is no matching personId in Address, perfectly lining up with the left join.
*/
SELECT p.firstName, p.lastName, a.city, a.state FROM Person p
LEFT JOIN Address a ON p.personId = a.personId
