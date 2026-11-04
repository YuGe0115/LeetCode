class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        result = []
        for i in range(len(sentences)):
            result.append(len(sentences[i].split()))
        return max(result)
        