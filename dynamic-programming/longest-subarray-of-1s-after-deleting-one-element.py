class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        left = 0
        right = 0
        count_0 = 0
        result = 0

        for right in range(n):
            if nums[right] == 1:
                pass
            elif nums[right] == 0:
                count_0 += 1

            while count_0 >= 2:
                if nums[left] == 0:
                    count_0 -= 1
                left += 1
            result = max(right - left, result)

        return result