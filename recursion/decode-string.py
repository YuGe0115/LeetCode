class Solution:
    def decodeString(self, s: str) -> str:
        count = 0
        string = ""
        stack = []

        for char in s:
            if char.isdigit():
                count = count * 10 + int(char)
            elif char == "[":
                stack.append((count,string))
                count = 0
                string = ""
            elif char == "]":
                num, stri = stack.pop()
                string = stri + num * string
            else:
                string += char
        return string

        
        