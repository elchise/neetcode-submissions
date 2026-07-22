from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0]*9
        cols = [0]*9
        boxes = [0]*9

        for i in range(len(board)):
            for j in range(len(board[0])):
                cur = board[i][j]
                if cur == '.':
                    continue

                cur = int(cur)
                if (rows[i] & (1 << cur)) or (cols[j] & (1 << cur)) or (boxes[((i//3)*3+j//3)] & (1 << cur)):
                    return False

                rows[i] |= (1 << cur)
                cols[j] |= (1 << cur)
                boxes[(i//3)*3+j//3] |= (1 << cur)

        return True