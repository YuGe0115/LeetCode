class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        result = float("-inf")
        if len(nums) == 1:
            return nums[0]
        ini = sum(nums[0:k])/k
        result = sum(nums[0:k])/k
        for i in range(1, len(nums)+1-k):
            result = result - (nums[i-1] - nums[i+k-1])/k
            if ini < result:
                ini = result
        return ini
            
        