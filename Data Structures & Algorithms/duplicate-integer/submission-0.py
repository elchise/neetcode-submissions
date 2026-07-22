class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         vals = set()
         for i in range(0, len(nums)):
            if nums[i] in vals:
                return True
            else:
                vals.add(nums[i])
            
        
         return False