# 41. First Missing Positive
## Language: C++

## Directions:
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

### Hints:

1. Think about how you would solve the problem in non-constant space. Can you apply that logic to the existing space?
2. We don't care about duplicates or non-positive integers
3. Remember that O(2n) = O(n)

## Takeaways:
1. No arrays can be created.
2. O(some integer * n) is fine.
3. Array is not sorted, and cannot be effectively sorted in O(n) time O(1) aux.


## Potential Ideas:
We know that no temporary array can be created for what's already been seen, the array cannot be sorted. Perhaps the values could be removed from the array in each pass? If that were the case we'd want to iterate backwards over the array to minimize the popping time.
