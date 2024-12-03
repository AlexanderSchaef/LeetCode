# 2109. Adding Spaces to a String
## Language: C++

Process:

My first thought was to use the find method for the vector, and if the index is found insert a space before the character. This takes far too much time, and searches the entire spaces vector every time resulting in a time complexity of at worst case O(n^2). Because the spaces array is sorted increasing, a pointer suffices for checking the next space.

This solution satisfies the problem and produces spaces in a new string at the specified positions and returns it.
