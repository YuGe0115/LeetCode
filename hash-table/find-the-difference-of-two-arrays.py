class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        result1 = []
        result2 = []

        for i in set1:
            if i not in set2:
                result1.append(i)
        
        for i in set2:
            if i not in set1:
                result2.append(i)  
        
        return [result1,result2]