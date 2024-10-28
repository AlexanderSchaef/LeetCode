# 4. Median of Two Sorted Arrays
## Language: Java
## Approach
My first thought was to simply combine the arrays and find the median, however combining the arrays would have taken O(m + n) time, and the question request O(log(m+n)), rendering this impossible.

My second thought was to determine if there was overlap between the two arrays, however this does not gurantee O(log(m+n)). It simplies the problem instance to a smaller length n, however the worst case of completely overlapping arrays would result in O(n+m) complexity still without binary search implementation. Which is when I had the idea of a binary search implementation.

I wasn't sure if a binary search could be correctly performed on two graphs while maintaining the correct sorted order, however it seemed possible. I set pointers to the start, end, and middle of both arrays, and proceeded to get stuck.

At which point, I reached 1 hour, and so I checked against the other solutions for the problem. I found similar methodology, and copied code for the remaining implementation work.
