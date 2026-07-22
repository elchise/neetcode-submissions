class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # n = len(nums) - k + 1
        # res = [float('-inf')] * n

        # for i in range(0, n):
        #     for j in range(i, i+k):
        #         print(i, j)
        #         res[i] = max(res[i], nums[j])
        
        # return res

        import heapq

        maxHeap = []
        res = []
        for i in range(len(nums)):
            heapq.heappush(maxHeap, (-nums[i], i))
            if i >= k-1:
                while (maxHeap[0][1] <= i-k):
                    heapq.heappop(maxHeap)
                maxVal, maxInd = maxHeap[0]
                res.append(-maxVal)
        return res
