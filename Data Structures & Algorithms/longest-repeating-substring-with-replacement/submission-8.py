class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1
            
            swaps = r - l + 1 - max(count.values())
            while swaps > k:
                count[s[l]] -= 1
                l += 1
                swaps = r - l + 1 - max(count.values())
            
            res = max(res, r - l + 1)

        return res