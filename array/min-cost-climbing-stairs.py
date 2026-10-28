class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        result = [0 for _ in range(n)]
        if n == 1:
            return 0
        # actually don't need this step because 2 <= length(in the Constraints section)

        if n == 2:
            return min(cost[0], cost[1])
        
        result[0] = cost[0]
        result[1] = cost[1]

        for i in range(2,n):
            result[i] = min(result[i-2] + cost[i], result[i-1] + cost[i])
        
        return min(result[-1],result[-2])


