from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((t, v))
        
        heap = []
        heapq.heappush(heap, (0, k))
        visited = set()
        res = 0
        while heap and len(visited) < n:
            time, node = heapq.heappop(heap)
            if node in visited:
                continue
            
            res = time
            visited.add(node)
            for t, nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(heap, (time + t, nei))
        
        return res if len(visited) == n else -1