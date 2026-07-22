class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}
        maxLength = 0
        l = 0
        
        for r in range(len(s)):
            if s[r] in charMap:
                l = max(l, charMap[s[r]] + 1)
            
            charMap[s[r]] = r
            maxLength = max(maxLength, r - l + 1)

        return maxLength

                
