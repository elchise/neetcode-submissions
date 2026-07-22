from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])

        # def dfs(r, c):
        #     if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0'):
        #         return
            
        #     grid[r][c] = '0'
        #     for dr, dc in directions:
        #         dfs(r+dr, c+dc)

        def bfs(r, c):
            q = deque()
            
            q.append((r, c))
            grid[r][c] = '0'

            while q:
                cr, cc = q.popleft()
                for dr, dc in directions:
                    nr, nc = cr+dr, cc+dc
                    if (nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == '0'):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = '0'
        
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    # dfs(i, j)
                    bfs(i, j)
                    count+=1
        
        return count

            