class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        result = set()
        for num in nums:
            result.add(num)
        return len(result) < len(nums)
        