class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I": 1, "V" : 5, "X" : 10, "L" : 50, "C": 100, "D" : 500, "M" : 1000}
        output = 0
        for i in range(len(s)):
            output = output + values[s[i]]
        for i in range(len(s)-1):
            if values[s[i]] < values[s[i+1]]:
                output = output - 2*values[s[i]]
            else:
                output
        return output