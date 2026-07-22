class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, i):
            if i == len(word)-1:
                return True

            res = False
            board[r][c] = "#"
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and word[i+1] == board[nr][nc]:
                    res = res or dfs(nr, nc, i+1)
            board[r][c] = word[i]

            return res
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        

        return False

        