import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) == 0:
            heapq.heappush(self.nums, val)
        elif len(self.nums) < self.k-1:
            heapq.heappush(self.nums, val)
            return 0
        elif len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val >= self.nums[0]:
            heapq.heappop(self.nums)
            heapq.heappush(self.nums, val)

        return self.nums[0]
        
