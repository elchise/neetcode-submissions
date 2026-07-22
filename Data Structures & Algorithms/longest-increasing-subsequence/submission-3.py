from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # n = len(nums)
        # lis = [1] *  n

        # for i in range(n-1, -1, -1): 
        #     for j in range(i, n):
        #         if nums[i] < nums[j]:
        #             lis[i] = max(lis[i], 1+lis[j])
        
        # return max(lis)

        n = len(nums)
        dp = [nums[0]]
        lis = 1

        for i in range(1, n):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
                lis += 1
            else:
                ind = bisect_left(dp, nums[i])
                dp[ind] = nums[i]

        return lis


