from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                cur = board[i][j]
                if cur == '.':
                    continue
                if cur in rows[i] or cur in cols[j] or cur in boxes[(i//3, j//3)]:
                    return False

                rows[i].add(cur)
                cols[j].add(cur)
                boxes[(i//3, j//3)].add(cur)
        
        return True