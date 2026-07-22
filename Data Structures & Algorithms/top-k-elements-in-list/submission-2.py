import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freqMap = defaultdict(int)

        for n in nums:
            freqMap[n] += 1
        
        for num, freq in freqMap.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            elif freq > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (freq, num))
        
        res = []
        while heap:
            _, num = heapq.heappop(heap)
            res.append(num)

        return res



        
