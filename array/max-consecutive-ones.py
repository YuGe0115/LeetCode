class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        left = 0
        max_len = 0
        result = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                left = right + 1
                max_len = max(max_len,result)
                result = 0
            else:
                result += 1
        return max(max_len, result) #last entry = 1!!!!!


        