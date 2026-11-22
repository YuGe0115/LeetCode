class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        # count_1 = 0
        # count_0 = 0
        # result = []

        # left = 0
        # right = 1
        
        # n = len(nums)
        
        # while count_0 <= k and right < n:
        #     if nums[right] == 0:
        #         count_0 += 1
        #         right += 1
        #     if nums[right] == 1:
        #         count_1 += 1
        #         right += 1
        
        # add_num = count_0 + count_1 - 1

        # while right<n:
            
        # result.append(add_nums)






        # new start
        j = 0
        count = 0
        result = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            if count <= k:
                result = max(result,i - j + 1)
            while count > k:
                j += 1
                if nums[j-1] == 0:
                    count -= 1
        return result

                

        
        
 
       