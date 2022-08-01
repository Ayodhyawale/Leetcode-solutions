class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        
        for row in range(9):
            for col in range(9):
                v = board[row][col]
                if v == '.': continue
                if v in rows[row] or v in cols[col] or v in squares[row // 3, col // 3]:
                    return False
                rows[row].add(v); cols[col].add(v); squares[row // 3, col // 3].add(v)
        
        return True

        
        