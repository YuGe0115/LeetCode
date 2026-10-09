class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = nums.copy()
        for i in range(n):
            result.append(nums[i])
        return result
        