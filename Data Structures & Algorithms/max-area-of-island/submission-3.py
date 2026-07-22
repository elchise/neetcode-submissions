class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        maxArea = 0
        def bfs(row, col):
            q = deque()
            q.append((row, col))
            grid[row][col] = 0
            area = 1

            while q:
                r, c = q.pop()

                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and grid[nr][nc] == 1:
                        area += 1
                        grid[nr][nc] = 0
                        q.append((nr, nc))
            
            return area
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    maxArea = max(bfs(i, j), maxArea)

        return maxArea
                



