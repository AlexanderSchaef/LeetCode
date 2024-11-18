class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        val = 1.0

        if n > 0:
            for i in range(n):
                val = val * x
            return val
        else: 
            for i in range(n - 1, -1):
                val = val * x
        return 1.0/val
