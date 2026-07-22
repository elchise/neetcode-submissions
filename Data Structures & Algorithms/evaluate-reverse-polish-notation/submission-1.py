class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = "+-*/"
        for c in tokens:
            if c not in operations:
                stack.append(int(c))
            elif c == "+":
                val = stack.pop() + stack.pop()
                stack.append(val)
            elif c == "-":
                num2 = stack.pop()
                val = stack.pop() - num2
                stack.append(val)
            elif c == "*":
                val = stack.pop() * stack.pop()
                stack.append(val)
                print(val)
            else:
                num2 = stack.pop()
                val = int(stack.pop() / num2)
                stack.append(val)
                    
        return stack.pop()
