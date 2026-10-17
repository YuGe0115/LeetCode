class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        n = len(asteroids)

        for i in range(n):
            if (not stack) or (stack and (stack[-1] * asteroids[i] > 0)):
                stack.append(asteroids[i])
            elif stack and (stack[-1] * asteroids[i] < 0):
                if stack[-1] < 0 and asteroids[i] > 0:
                    stack.append(asteroids[i])
                if stack[-1] > 0 and asteroids[i] < 0:
                    if stack[-1] + asteroids[i] > 0:
                        continue
                    elif stack[-1] + asteroids[i] == 0:
                        stack.pop()
                    else:
                        while stack and stack[-1] > 0 and (stack[-1] + asteroids[i] <0):
                            stack.pop()
                        if not stack or stack[-1] < 0 :
                            stack.append(asteroids[i])
                        elif stack[-1] + asteroids[i] == 0:
                            stack.pop()
        
        return stack

        