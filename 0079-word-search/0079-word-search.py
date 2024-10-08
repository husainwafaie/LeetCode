class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def find_word(board, word, ind1, ind2, index):
            if index == len(word):
                return True
            if ind1 - 1 >= 0 and board[ind1 - 1][ind2] == word[index]:
                board[ind1 - 1][ind2] = ""
                if find_word(board, word, ind1 - 1, ind2, index + 1):
                    return True
                board[ind1 - 1][ind2] = word[index]
            if ind1 + 1 < len(board) and board[ind1 + 1][ind2] == word[index]:
                board[ind1 + 1][ind2] = ""
                if find_word(board, word, ind1 + 1, ind2, index + 1):
                    return True
                board[ind1 + 1][ind2] = word[index]
            if ind2 - 1 >= 0 and board[ind1][ind2 - 1] == word[index]:
                board[ind1][ind2 - 1] = ""
                if find_word(board, word, ind1, ind2 - 1, index + 1):
                    return True
                board[ind1][ind2 - 1] = word[index]
            if ind2 + 1 < len(board[0]) and board[ind1][ind2 + 1] == word[index]:
                board[ind1][ind2 + 1] = ""
                if find_word(board, word, ind1, ind2 + 1, index + 1):
                    return True
                board[ind1][ind2 + 1] = word[index]
            

        for i in range(len(board)):
            for k in range(len(board[0])):
                if board[i][k] == word[0]:
                    board[i][k] = ""
                    if find_word(board, word, i, k, 1):
                        return True
                    board[i][k] = word[0]

        return False
