class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        st = list(s)

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            if c == ')':
                if stack:
                    stack.pop()
                else:
                    st[i] = ''
            
        while stack:
            st[stack.pop()] = ''

        return ''.join(st)
                    
