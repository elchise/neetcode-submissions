class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        op = '+'
        cur = 0
        prev = None
        s = s.replace(" ", "")

        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                cur = cur * 10 + int(c)
            
            if not c.isdigit() or i == len(s) - 1:
                if op == '+':
                    stack.append(cur)
                elif op == '-':
                    stack.append(-cur)
                elif op == '*':
                    prv = stack.pop()
                    stack.append(prv * cur)
                else:
                    prv = stack.pop()
                    stack.append(int(prv / cur))
                op = c
                cur = 0

        return sum(stack)