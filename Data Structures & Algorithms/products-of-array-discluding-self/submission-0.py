class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        pre = [0]*(len(nums))
        post = [0]*(len(nums))
        pre[0] = nums[0]
        for i in range(1, len(nums)):
            pre[i] = pre[i-1]*nums[i]
        print(pre)
        
        post[len(nums)-1] = nums[len(nums)-1]
        for i in range(len(nums)-2,-1, -1):
            post[i] = post[i+1]*nums[i]
        
        print(post)
        
        res = [0]*(len(nums))
        res[0] = post[1]
        res[len(nums)-1] = pre[len(nums)-2]
        for i in range(1, len(nums)-1):
            res[i] = pre[i-1]*post[i+1]
        return res

        return res
