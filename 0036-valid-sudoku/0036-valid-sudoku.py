class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            found = set()
            for k in range(9):
                if board[i][k] in found:
                    return False
                elif board[i][k] != ".":
                    found.add(board[i][k])
        for i in range(9):
            found = set()
            for k in range(9):
                if board[k][i] in found:
                    return False
                elif board[k][i] != ".":
                    found.add(board[k][i])
        intervals = [[0, 3], [3, 6], [6, 9]]
        for i1, i2 in intervals:
            for k1, k2 in intervals:
                found = set()
                for i in range(i1, i2):
                    for k in range(k1, k2):
                        if board[k][i] in found:
                            return False
                        elif board[k][i] != ".":
                            found.add(board[k][i])
        return True