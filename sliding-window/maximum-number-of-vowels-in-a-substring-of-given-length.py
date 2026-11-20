class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        n = len(s)

        result = 0
        for i in range(0,k):
            if s[i] in vowels:
                result += 1
        max_result = result
        for i in range(1,n-k+1):
            if s[i-1] in vowels:
                result -= 1
            if s[i+k-1] in vowels:
                result += 1

            if result > max_result:
                max_result = result
        return max_result

        