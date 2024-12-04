# 511. Game Play Analysis I
## Language: MySQL

First appoach:

Sub-select the table searching for the minimum with a WHERE clause to reduce the outer SELECT to only return the minimum event time.

Second Approach:

Use the GROUP BY functionality to remove the sub-select
