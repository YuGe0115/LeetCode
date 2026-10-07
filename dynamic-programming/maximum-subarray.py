class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        sum_num = 0
        max_sum = nums[0]

        for num in nums:
            if sum_num < 0:
                sum_num = 0

            sum_num += num

            max_sum = max(max_sum, sum_num)

        return max_sum

        