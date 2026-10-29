class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum_s = 0
        sum_t = 0
        for i in range(len(s)):
            sum_s += ord(s[i])
        for j in range(len(t)):
            sum_t += ord(t[j])
        
        return chr(sum_t - sum_s)
        