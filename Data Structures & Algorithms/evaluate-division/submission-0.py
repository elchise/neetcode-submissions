from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i in range(len(equations)):
            a, b = equations[i]
            adj[a].append((b, values[i]))
            adj[b].append((a, 1/values[i])) 

        def bfs(num, denom):
            if num not in adj or denom not in adj:
                return -1

            q = deque([(num, 1)])
            visited = set()
            while q:
                curNum, curVal = q.popleft()
                visited.add(curNum)
                for d, v in adj[curNum]:
                    nextVal = curVal * v
                    if d == denom:
                        return nextVal
                    
                    if d not in visited:
                        q.append([d, nextVal])

            return -1

        res = []
        for num, denom in queries:
            res.append(bfs(num, denom))
        
        return res

