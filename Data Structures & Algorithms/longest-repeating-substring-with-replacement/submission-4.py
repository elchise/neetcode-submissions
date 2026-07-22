class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        count = collections.defaultdict(int)
        curMax = 0

        for r in range(len(s)):
            count[s[r]]+=1
            curMax = max(count[s[r]], curMax)

            while r-l+1 - curMax > k:
                # if count[s[l]] == curMax:
                #     curMax -= 1

                count[s[l]] -= 1
                l += 1
                
            res = max(res, r-l+1)
        
        return res
