class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy = [1] * len(ratings) #初始化，所有孩子分到的糖初始值都是1
        for i in range(0,len(ratings)-1):
            if ratings[i] < ratings[i+1]:
                candy[i+1] = candy[i] + 1
        
        #为什么这次不能也从左往右呢？因为比如遇到[2,6,3,1]这种情况，最得到的糖果列表就是[1,2,2,1]
        for j in range(len(ratings)-2,-1,-1): #从右向左
            if ratings[j] > ratings[j+1] and candy[j] <= candy[j+1]:
                candy[j] = candy[j+1] + 1
        return sum(candy)