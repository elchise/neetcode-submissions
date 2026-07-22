class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # import heapq

        # maxHeap = []
        # res = []
        # for i in range(len(nums)):
        #     heapq.heappush(maxHeap, (-nums[i], i))
        #     if i >= k-1:
        #         while (maxHeap[0][1] <= i-k):
        #             heapq.heappop(maxHeap)
        #         maxVal, maxInd = maxHeap[0]
        #         res.append(-maxVal)
        # return res

        res = []
        q = collections.deque()
        l = r = 0
        while r < len(nums):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
            
            if l > q[0]:
                q.popleft()

            if r == l + k - 1:
                res.append(nums[q[0]])
                l += 1

            r += 1
            
        return res
                

