class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # 用列表模拟栈，它记录“顺序”，特别适合处理“嵌套”或“配对”的问题
        mapping = {')': '(', ']': '[', '}': '{'}  # 闭括号到开括号的映射
        
        for char in s:
            if char in mapping:  # 如果是闭括号
                if not stack or stack.pop() != mapping[char]:  # pop是取最右一个元素的意思；这里的判断条件是栈空或不匹配
                    return False
            else:  # 如果是开括号
                stack.append(char)
        
        return len(stack) == 0  # 栈空表示有效
        