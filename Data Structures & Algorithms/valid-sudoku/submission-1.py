class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=collections.defaultdict(set)
        col=collections.defaultdict(set)
        grid=collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                digit=board[r][c]
                if digit==".":
                    continue
                if digit in row[r] or digit in col[c] or digit in grid[(r//3,c//3)]:
                    return False
                row[r].add(digit)
                col[c].add(digit)
                grid[(r//3,c//3)].add(digit)
        return True
