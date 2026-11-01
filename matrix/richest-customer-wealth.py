class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        n = len(accounts)
        result = []
        for i in range(n):
            result.append(sum(accounts[i]))
        return max(result)
            
        