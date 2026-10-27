class Solution:
    def rob(self, nums: list[int]) -> int:
        total = [0 for _ in range(len(nums))]
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        elif len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])
        else:
            total[0] = nums[0]
            total[1] = nums[1]
            total[2] = max(total[0] + nums[2], total[1])
            for i in range(2,len(nums)):
                total[i] = max(nums[i] + total[i-2], nums[i] + total[i-3], total[i-1])
            return max(total)
            #no need to trace back