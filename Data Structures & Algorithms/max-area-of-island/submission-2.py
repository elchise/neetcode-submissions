class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        maxArea = 0
        def bfs(row, col):
        
            q = deque()
            q.append((row, col))
            area = 0

            while q:
                r, c = q.pop()
                
                if (r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0):
                    continue
                
                grid[r][c] = 0
                area += 1
                for dr, dc in DIRS:
                    q.append((r+dr, c+dc))
            
            return area
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    maxArea = max(bfs(i, j), maxArea)

        return maxArea
                



