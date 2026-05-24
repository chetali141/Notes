class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        if not self.checkRows(board):
            print("duplicate in row")
            return False

        if not self.checkColumns(board):
            print("duplicate in column")
            return False

        if not self.checkSquare(board):
            print("duplicate in square")
            return False
        
        return True

    def checkRows(self, board):
        for i in range(0,9):
            dict = {}
            for j in range(0,9):
                if board[i][j] == '.':
                    continue
                else:
                    if board[i][j] in dict:
                        return False
                    else:
                        dict[board[i][j]] = 1
        return True
    
    def checkColumns(self, board):
        for i in range(0,9):
            dict = {}
            for j in range(0,9):
                if board[j][i] == '.':
                    continue
                else:
                    if board[j][i] in dict:
                        return False
                    else:
                        dict[board[j][i]] = 1
        return True

    def checkSquare(self, board):
        if not self.check(board, 3, 3):
            return False

        if not self.check(board, 3, 6):
            return False
        
        if not self.check(board, 3, 9):
            return False

        if not self.check(board, 6, 3):
            return False

        if not self.check(board, 6, 6):
            return False
        
        if not self.check(board, 6, 9):
            return False

        if not self.check(board, 9, 3):
            return False

        if not self.check(board, 9, 6):
            return False
        
        if not self.check(board, 9, 9):
            return False

        return True

    def check(self, board, row, col):
        dict = {}
        i = row - 3
        while i < row:
            j = col - 3
            while j < col:
                if board[i][j] == '.':
                    j += 1
                else:
                    if board[i][j] in dict:
                        print(i, j, board[i][j])
                        return False
                    else:
                        dict[board[i][j]] = 1
                        j += 1
            i += 1
        return True
