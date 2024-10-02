class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        lst  = []
        def helper(x, y):
            count = 0
            up = x - 1 >= 0
            down = x + 1 < len(board)
            right = y + 1 < len(board[0])
            left = y - 1 >= 0

            if up and right and board[x - 1][y + 1] == 1:
                count += 1
            if up and board[x - 1][y] == 1:
                count += 1
            if up and left and board[x - 1][y - 1] == 1:
                count += 1
            if left and board[x][y - 1] == 1:
                count += 1
            if right and board[x][y + 1] == 1:
                count += 1
            if down and right and board[x + 1][y + 1] == 1:
                count += 1
            if down and left and board[x + 1][y - 1] == 1:
                count += 1
            if down and board[x + 1][y] == 1:
                count += 1
            
            return count

        dct = {}

        for i in range(len(board)):
            for k in range(len(board[0])):
                num = helper(i, k)
                if board[i][k] == 1:
                    if num < 2 or num > 3:
                        lst.append([[i, k], 0])
                else:
                    if num == 3:
                        lst.append([[i,k], 1])    
        for index, num in lst:
            board[index[0]][index[1]] = num