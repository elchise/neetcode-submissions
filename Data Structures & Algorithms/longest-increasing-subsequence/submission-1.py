class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        subseq = {}
        def dfs(i, prev, nums):
            if i == len(nums):
                return 0
            
            # if i in subseq:
            #     print('i')
            #     return subseq[i]
            
            if prev == -1 or nums[i] > nums[prev]:
                subseq[i] = max(dfs(i+1, i, nums)+1, dfs(i+1, prev, nums))
                return subseq[i]
            
            # subseq[i] = dfs(i+1, prev, nums)
            return dfs(i+1, prev, nums)
        
        return dfs(0, -1, nums)
            