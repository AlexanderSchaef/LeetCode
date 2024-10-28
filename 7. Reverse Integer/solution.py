class Solution:
    def reverse(self, x: int) -> int:

        
        
        negative = False
        if x < 0:
            negative = True
            x = -x
        solution = str(x)[::-1]
        if int(solution) > 2147483647:
            return 0
        if negative:
            return -int(solution)
        return int(solution)
