class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # DP
        dp = [float("inf")for _ in range(amount + 1)]

        #base case
        dp[0] = 0

        #recurrence
        for i in range(1,amount+1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        
        return dp[-1] if dp[-1] != float("inf") else -1
        #runtime: array with n+1 length, for each array O(m) where m = len(coins)
        # Total: O(mn)
        