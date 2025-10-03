class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
    mapping = {')': '(', ']': '[', '}': '{'}  # 闭括号到开括号的映射
    
    for char in s:
        if char in mapping:  # 如果是闭括号
            if not stack or stack.pop() != mapping[char]:  # 栈空或不匹配
                return False
        else:  # 如果是开括号
            stack.append(char)
    
    return len(stack) == 0  # 栈空表示有效
        