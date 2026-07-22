class Solution:
    def isValid(self, s: str) -> bool:
        openers="({["
        closers=")}]"
        stack = []
        for char in s:
            if char in openers:
                stack.append(char)
            elif char in closers:
                if len(stack) <= 0:
                    return False
                op = stack.pop()
                if openers.index(op) != closers.index(char):
                    return False
        if len(stack) != 0:
            return False
        return True