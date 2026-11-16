class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)

        left = 0
        right = len(s) - 1

        re = set("aeiouAEIOU")

        for char in s:
            while left < right:
                if s[left] not in re:
                    left += 1
                elif s[right] not in re:
                    right -= 1
                else:
                    s[left], s[right] = s[right],s[left]
                    left += 1
                    right -= 1
        
        return "".join(s)
        