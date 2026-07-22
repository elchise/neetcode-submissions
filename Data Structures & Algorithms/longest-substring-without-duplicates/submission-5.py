class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}
        l = 0
        res = 0
        for r in range(len(s)):
            c = s[r]
            if c in charMap and charMap[c] >= l:
                l = charMap[c] + 1
            charMap[c] = r
            res = max(res, r - l + 1)
        return res


                
