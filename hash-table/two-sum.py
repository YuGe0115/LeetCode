class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}  # 字典
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i  # 存入当前元素