class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #使用相向双指针思想，降低时间复杂度，主要思想是提升计算的效率
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] == target:
                break
        return [left+1, right+1]
        