class Solution:
    def numTilings(self, n: int) -> int:
        # dynamic programming
        dp = [0 for _ in range(n)]
        dp_upper = [0 for _ in range(n)]
        dp_down = [0 for _ in range(n)]

        mol = 10**9 + 7 #int not float

        if n == 1:
            return 1
        if n == 2:
            return 2

        #base case:
        dp[0] = 1
        dp_upper[0] = 1
        dp_down[0] = 1

        dp[1] = 2
        dp_upper[1] = 2
        dp_down[1] = 2


        for i in range(2,n):
            dp[i] = (dp_upper[i-2] + dp_down[i-2] + dp[i-1] + dp[i-2]) % mol
            dp_upper[i] = (dp_down[i-1] + dp[i-1]) % mol
            dp_down[i] = (dp_upper[i-1] + dp[i-1]) % mol

        return dp[-1]
