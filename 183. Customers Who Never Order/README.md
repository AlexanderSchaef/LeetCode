# 183. Customers Who Never Order
## Language MySQL

Question:

Write a solution to find all customers who never order anything.

Approach:

A customer who never orders anything will not have their id in the Orders table. This search can be accomplished with either a join or a sub-select statement, I chose a sub-select statement as it is slightly faster in this case. Search for entries in Customer with no corresponding foreign key customerId reference in table Orders
