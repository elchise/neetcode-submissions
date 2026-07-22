class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        k = len(nums)-1
        j = i+1
        sol = []

        while (i < len(nums)-2):
            cur = -1*nums[i]
            j = i+1
            k = len(nums)-1
            while(j<k):
                if nums[j] + nums[k] < cur:
                    j+=1
                elif nums[j] + nums[k] > cur:
                    k-=1
                else:
                    if([nums[i], nums[j], nums[k]] not in sol):
                        sol.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1                    
            i+=1

        return (sol)