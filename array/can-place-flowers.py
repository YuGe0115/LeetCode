class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool: #返回一个布尔值
        
        # 思路来源于CSDN，3个连续的0可以种一个，4个连续的0可以种1个，5个连续的0可以种2个……
        # 注意，还要考虑两端是0的情况！
        flowerbed = [0] + flowerbed + [0]
        result = []
        final = []
        count = 0

        for i in flowerbed:
            if i == 0:
                count += 1
            else:
                if i == 1 and count >= 3:
                    result.append(count)
                count = 0
        
        # 最后一段全都是0没有1作为一个截断，那么按照现有的逻辑是不会更新进result的，还需要再优化一下
        if count >= 3:
            result.append(count)

        for j in result:
            final.append((j-1)//2) #整除运算，自动实现向下取整
        
        return sum(final) >= n
        