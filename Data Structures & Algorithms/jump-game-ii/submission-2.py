class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # dp = [float('inf')] * n
        # dp[-1] = 0

        # for i in range(n-1, -1, -1):
        #     end = min(n, i + nums[i] + 1)
        #     for j in range(i+1, end):
        #         dp[i] = min(dp[i], dp[j] + 1)
        
        # return dp[0]

        r = 0
        l = 0
        res = 0

        while r < n-1:
            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])
            l = r+1
            r = farthest 
            res += 1
        return res
