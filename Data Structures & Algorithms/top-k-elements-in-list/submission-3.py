import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)
        buckets = [[] for _ in range(len(nums))]

        for n in nums:
            freqMap[n] += 1

        for num, freq in freqMap.items():
            buckets[freq - 1].append(num)
        
        res = []
        i = len(buckets) -1
        
        while len(res) < k and i >= 0:
            res.extend(buckets[i])
            i -= 1
        
        return res
            
        

        
        
        # heap = []
        # freqMap = defaultdict(int)

        # for n in nums:
        #     freqMap[n] += 1
        
        # for num, freq in freqMap.items():
        #     if len(heap) < k:
        #         heapq.heappush(heap, (freq, num))
        #     elif freq > heap[0][0]:
        #         heapq.heappop(heap)
        #         heapq.heappush(heap, (freq, num))
        
        # res = []
        # while heap:
        #     _, num = heapq.heappop(heap)
        #     res.append(num)

        # return res



        
