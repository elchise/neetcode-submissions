class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curMax = 0
        globalMax = nums[0]

        for num in nums:
            curMax = max(curMax + num, num)
            globalMax = max(globalMax, curMax)
        
        return globalMax
