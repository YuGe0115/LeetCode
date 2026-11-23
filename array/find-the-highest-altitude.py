class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        start = 0
        height = 0
        for i in range(len(gain)):
            height = height + gain[i]
            start = max(start, height)
        return start
        