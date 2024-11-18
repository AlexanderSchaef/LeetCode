# 14. Longest Common Prefix
## Language: C++

First solution: check the char at some position until they're not all equal, and return the chars seen

You only have to check the shortest length string

Program works, but it's a naive approach and runs very slowly.

Second solution:

Idea: If the vector were sorted, you'd only have to compare two strings. This solution is much quicker, although the time now depends on the speed of the sorting algorithm used.


### Complexity Analysis
1. The built in std::sort runs in O(n log n) time where n is the number of elements
2. The for loop runs through the length of the shortest of the two strings at the beginning and the end of the sorted list, which I'll denote m

The program therefore runs in O(n * log n + m) time and uses O(1) auxilliary and space complexity

