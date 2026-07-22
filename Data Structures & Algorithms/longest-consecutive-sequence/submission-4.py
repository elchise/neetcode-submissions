class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort = nums.sort()
        res = 0

        temp = 1
        for i in range(0, len(nums)):
            if i == 0:
                res=1
            elif nums[i]-nums[i-1] == 1:
                temp+=1
                if temp > res:
                    res = temp
            elif nums[i]-nums[i-1] == 0:
                continue
            else:
                temp=1

        return res
