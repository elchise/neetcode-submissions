class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(board), len(board[0])
        # seen = set()
        def dfs(r, c, word, i):
            if i == len(word):
                return True

            # seen.add((r, c))
            board[r][c] = "."
            exists = False
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == word[i]:
                    if dfs(nr, nc, word, i + 1):
                        exists = True
            # seen.remove((r, c))
            board[r][c] = word[i - 1]
            return exists
            
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, word, 1):
                        return True
        
        return False
        

