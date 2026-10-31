class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        n= len(candies)
        result = []
        max_num = max(candies)
        for i in range(n):
            if candies[i] + extraCandies >= max_num:
                result.append(True)
            else:
                result.append(False)
        return result
        
            
        