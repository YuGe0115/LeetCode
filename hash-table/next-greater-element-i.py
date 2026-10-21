class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # first, make a hashmap from nums2 for nums1 to do later query
        decreasing_stack = []
        query = {}

        for num in nums2:
            while decreasing_stack and num > decreasing_stack[-1]:
                query[decreasing_stack[-1]] = num
                decreasing_stack.pop()
            decreasing_stack.append(num)
        
        result = []
        for num in nums1:
            result.append(query.get(num,-1))

        return result

        