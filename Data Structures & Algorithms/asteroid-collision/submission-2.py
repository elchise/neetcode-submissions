class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                if len(stack) == 0 or stack[-1] < 0:
                    stack.append(asteroid)
                elif stack[-1] == abs(asteroid):
                    stack.pop()
                else:
                    explode = False
                    while len(stack) > 0 and stack[-1] > 0:
                        if (stack[-1]) < abs(asteroid):
                            stack.pop()
                        elif stack[-1] == abs(asteroid):
                            explode = True
                            stack.pop()
                            break
                        else:
                            explode = True
                            break
                    if not explode:
                        stack.append(asteroid)
                
        
        return stack

