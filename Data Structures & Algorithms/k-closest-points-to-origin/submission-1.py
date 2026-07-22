import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minHeap = []
        for x,y in points:
            dist = math.sqrt(x**2+y**2)
            heapq.heappush(minHeap, (-dist, x, y))
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return [point[1:] for point in minHeap]