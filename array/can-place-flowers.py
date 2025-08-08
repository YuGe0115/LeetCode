class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool: #返回一个布尔值
        
        # 思路来源于CSDN，3个连续的0可以种一个，4个连续的0可以种1个，5个连续的0可以种2个……
        result = []
        final = []
        count = 0
        for i in flowerbed:
            if i == 0:
                count += 1
            elif i == 1 and count >= 3:
                result.append(count)
                count = 0
            else:
                count = 0

        for j in result:
            final.append((j-1)//2) #整除运算，自动实现向下取整
        
        return sum(final) >= n
        