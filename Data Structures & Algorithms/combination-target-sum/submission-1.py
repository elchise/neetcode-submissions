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


        # def dfs(i, cur, total):
        #     if total == target:
        #         res.append([i for i in cur])
        #         return 
        #     if i >= len(nums) or total > target:
        #         return
            
        #     dfs(i, cur + [nums[i]], total+nums[i])
        #     dfs(i + 1, cur, total)
         
        dfs(0, [], 0)
        return res
            

