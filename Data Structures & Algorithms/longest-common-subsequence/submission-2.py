class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        
        n = len(text1)
        m = len(text2)
        # dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        cur = [0] * (m + 1)
        prv = [0] * (m + 1)

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if text1[i] == text2[j]:
                    cur[j] = 1 + prv[j+1]
                else:
                    cur[j] = max(cur[j+1], prv[j])
            prv, cur = cur, prv
        
        return prv[0]

        