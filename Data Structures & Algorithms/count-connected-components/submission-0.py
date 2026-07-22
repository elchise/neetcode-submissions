class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()

        def bfs(node):
            q = deque()
            count = 0
            q.append(node)

            while q:
                n = q.popleft()
                visited.add(n)
                for nei in adj[n]:
                    if nei not in visited:
                        visited.add(n)
                        q.append(nei)
    
        count = 0
        for i in range(n):
            if i not in visited:
                bfs(i)
                count += 1

        return count


