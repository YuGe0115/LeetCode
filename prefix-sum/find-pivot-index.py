class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        all_result = sum(nums)
        cumulated = 0
        for i in range(len(nums)):
            cumulated += nums[i]
            if cumulated - nums[i] == all_result - cumulated:
                return i
        return -1
        