class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = [0] * len(nums)
        sumnum = 0
        for i in range(len(nums)):
            sumnum += nums[i]
            result[i] = sumnum
        return result

        