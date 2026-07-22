class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        q = deque()
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(len(board)):
            if board[i][0] == 'O':
                q.append((i, 0))
            if board[i][COLS-1] == 'O':
                q.append((i, COLS-1))

        for i in range(len(board[0])):
            if board[0][i] == 'O':
                q.append((0, i))
            if board[ROWS-1][i] == 'O':
                q.append((ROWS-1, i))
        
        while q:
            r, c = q.popleft()
            if not (0 <= r < ROWS) or not (0 <= c < COLS) or board[r][c] != 'O':
                continue
            board[r][c] = 'T'
            for dr, dc in DIRS:
                q.append((r+dr, c+dc))
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'

