class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # curSum = maxSum = nums[0]
        # for i in range(1, len(nums)):
        #     if curSum < 0:
        #         curSum = nums[i]
        #     else:
        #         curSum += nums[i]
        #     maxSum = max(curSum, maxSum)

        dp = [i for i in nums]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i], dp[i]+dp[i-1])
        return max(dp)


        return maxSum
