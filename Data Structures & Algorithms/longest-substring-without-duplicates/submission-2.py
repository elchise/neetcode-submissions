class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curChar = set()
        maxLength = 0
        l = 0

        for r in range(len(s)):
            while s[r] in curChar:
                curChar.remove(s[l])
                l += 1

            curChar.add(s[r])
            maxLength = max(maxLength, r-l+1)
            print(l, r)

        return maxLength
