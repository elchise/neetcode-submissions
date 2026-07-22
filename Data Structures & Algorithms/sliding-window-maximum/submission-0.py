class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums) - k + 1
        res = [float('-inf')] * n

        for i in range(0, n):
            for j in range(i, i+k):
                print(i, j)
                res[i] = max(res[i], nums[j])
        
        return res

