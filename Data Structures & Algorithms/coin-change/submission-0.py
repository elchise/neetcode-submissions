class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                a = i - c
                if a >= 0:
                    dp[i] = min(dp[a] + 1, dp[i])

        if dp[amount] != amount + 1:
            return dp[amount]

        return -1