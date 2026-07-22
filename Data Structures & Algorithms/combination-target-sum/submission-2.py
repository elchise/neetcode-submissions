class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append([i for i in cur])
                return
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                dfs(j, cur + [nums[j]], total + nums[j])
         
        dfs(0, [], 0)
        return res
            

