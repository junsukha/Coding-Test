class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            if board[i][0] == 'O':
                self.make_one(board, i, 0)
            if board[i][len(board[0])-1] == 'O':
                self.make_one(board, i , len(board[0])-1)
                
        for j in range(len(board[0])):
            if board[0][j] == 'O':
                self.make_one(board, 0, j)
            if board[len(board)-1][j] == 'O':
                self.make_one(board, len(board)-1, j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 1:
                    board[i][j] = 'O'  
            
    def make_one(self, board, i ,j):
        
        # if i < 0 or i >= len(board) or board[i][j] == 'X' or board[i][j] == 1 or j >=0 or j < -len(board):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or  board[i][j] == 'X' or board[i][j] == 1:
            return
        
        board[i][j] = 1
        self.make_one(board, i+1, j)
        self.make_one(board, i-1, j)
        self.make_one(board, i, j+1)
        self.make_one(board, i, j-1)