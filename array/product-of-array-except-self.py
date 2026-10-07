class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        left = [0]*n
        left[0] = 1

        left_begin = 1
        for i in range(1,n):
            left_begin = left_begin * nums[i-1]
            left[i] = left_begin
        
        right = [0]*n
        right[n-1] = 1
        right_begin = 1


        for j in reversed(range(n-1)):
            right_begin = right_begin * nums[j+1]
            right[j] = right_begin
        
        result = [0]*n
        for k in range(n):
            result[k] = left[k] * right[k]
        return result

