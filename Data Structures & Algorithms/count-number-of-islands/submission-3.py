from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        rows, cols = len(grid), len(grid[0])
        res = 0

        def bfs(row, col):
            q = deque()
            q.append((row, col))

            while q:
                r, c = q.popleft()
                grid[r][c] = '0'
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                        q.append((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    res += 1
                    bfs(r, c)
        
        return res

