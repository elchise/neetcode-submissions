class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i in range(0, len(nums)):
            if(target-nums[i]) in values:
                return [values[target-nums[i]][0], i]
            if not nums[i] in values:
                values[nums[i]] = []
            values[nums[i]].append(i)
            

