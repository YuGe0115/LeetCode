class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix
        prefix = {0:1} #dictionary!!! prefix may repeat
        # prefix = {cumulation:frequency}. At the start point, no value is added so the start number is 0.
        cumulation = 0
        count = 0

        for i in range(len(nums)):
            cumulation += nums[i]
            query = cumulation - k
            
            if query in prefix:
                count += prefix[query]
            
            if cumulation in prefix:
                prefix[cumulation] +=1
            if cumulation not in prefix:
                prefix[cumulation] = 1
        
        return count

        #Method 2: 双指针加滑动窗口在有负数存在的时候行不通

        


        