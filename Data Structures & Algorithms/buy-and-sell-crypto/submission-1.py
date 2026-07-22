class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l, r = 0, 1

        while r < len(prices):
            buy, sell = prices[l], prices[r]
            
            if buy < sell:
                maxProfit = max(sell - buy, maxProfit)
            else:
                l = r
            r+=1
        return maxProfit
