class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # dp = [[0 for _ in range(2)] for _ in range(n+1)]
        # dp[n][0] = dp[n][1] = 0


        # for i in range(n-1, 0, -1):
        #     if prices[i] > prices[i-1]:
        #         dp[i][1] += prices[i] - prices[i-1]

        dp = {}
        def dfs(i, buying):
            if i >= n:
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(cooldown, buy)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(cooldown, sell)
            
            return dp[(i, buying)]
        
        return dfs(0, True)


        