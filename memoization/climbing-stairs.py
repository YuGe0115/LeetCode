class Solution:
    def climbStairs(self, n: int) -> int:
        result = [0 for _ in range(n)]
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        result[0] = 1
        result[1] = 2

        for i in range(2,n):
            result[i] = result[i-1] + result[i-2]
        
        return result[-1]

        