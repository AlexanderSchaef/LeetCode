# 2825. Make String a Subsequence Using Cyclic Increments
## Language: Python

Approach:

Find and store the possible values for each character in str1 and it's alternate cyclic increment value. Perform a linear check for the subsequence, grabbing 0 or 1 characters from the position in str1 to determine if str2 can be created from a linear path through the str1 and it's increment positions

Time complexity: O(n) where n is the length of str1

Note, invariate on str2's length, as a subsequence must be strictly less than its parent sequence
