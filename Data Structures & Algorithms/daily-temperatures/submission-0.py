class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                day, temp = stack.pop()
                res[day] = i - day
            
            stack.append((i, temperatures[i]))
        
        return res