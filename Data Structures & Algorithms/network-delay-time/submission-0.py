import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        edges = collections.defaultdict(list)
        for ui, vi, ti in times:
            edges[ui].append((vi, ti))
        
        minHeap = [(0, k)]
        visited = set()
        total = 0

        while minHeap:
            dist, cur = heapq.heappop(minHeap)
            if cur in visited:
                continue

            visited.add(cur)
            total = max(dist, total)

            for nextNode, nextDist in edges[cur]:
                if nextNode not in visited:
                    heapq.heappush(minHeap, (dist+nextDist, nextNode))
        
        if len(visited) == n:
            return total
        
        return -1