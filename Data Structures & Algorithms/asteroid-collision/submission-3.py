class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while a < 0 and stack and stack[-1] > 0:
                if stack[-1] < abs(a):
                    stack.pop()
                elif stack[-1] == abs(a):
                    a = 0
                    stack.pop()
                else:
                    a = 0
            
            if a != 0:
                stack.append(a)
            
        return stack

