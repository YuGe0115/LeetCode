class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        else:
            if x > 0:
                sign = 1
            elif x < 0:
                sign = -1
            x = abs(x)
            string = str(x)
            string1 = string[::-1]
            string2 = int(string1)
            return sign * string2
        
        