class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        m = float('inf')
        for p in prices:
            m = min(p, m)
            res = max(p - m, res)
        
        return res
        