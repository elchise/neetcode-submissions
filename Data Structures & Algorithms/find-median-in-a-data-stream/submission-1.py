import heapq

class MedianFinder:

    def __init__(self):
        self.minHeap, self.maxHeap = [], []
        
    def addNum(self, num: int) -> None:
        if self.maxHeap and -self.maxHeap[0] > num:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
        
        if len(self.maxHeap) < len(self.minHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        if len(self.maxHeap) > len(self.minHeap)+1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

        print(self.minHeap, self.maxHeap)
        
    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + -self.maxHeap[0])/2
        
        return -self.maxHeap[0]
        
        