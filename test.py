from collections import deque

def moves(n, startRow, startCol, endRow, endCol, bishopRow, bishopCol):
    # Write your code here
    # 0 = empty
    # 1 = threatend by bishop
    # 2 = knight
    # 3 = ending point
    # 4 = bishop
   
    #what if ending point is one of threatend or bishop's position
    board = [ [0 for _ in range(n)] for _ in range(n)]
    board[startRow][startCol] = 2
    board[endRow][endCol] = 3
    
    
    for i in range(n):
        for j in range(n):
            if (i - bishopRow) == (j - bishopCol) or (bishopRow - i) == (j - bishopCol) :
                board[i][j] = 1
    board[bishopRow][bishopCol] = 4
    
    q = deque()
    curRow = startRow
    curCol = startCol
    q.append((board, 0, curRow, curCol))
    original = 0
    while q:
        matrix, count, curRow, curCol = q.popleft()
        if curRow == endRow and curCol == endCol:
            print(count)
            break
        if count > 20:
            print(count)
            return -1
        
        newCount = count+1
        matrix[curRow][curCol] = 0
        matrix_copy = [row[:] for row in matrix]
       
       
        
        
        # bishop is dead
        if (matrix_copy[bishopRow][bishopCol] != 4):
            # move right up up
            curRow1 = curRow - 2
            curCol1 = curCol + 1
            if (curRow1 > - 1 and curCol1 < n):
                matrix_copy = [row[:] for row in matrix]
                
                original = matrix_copy[curRow1][curCol1]
                matrix_copy[curRow1][curCol1] = 2
                
                q.append((matrix_copy,newCount, curRow1, curCol1))
                matrix_copy[curRow1][curCol1] = original
            # move right down down
            curRow2 = curRow + 2
            curCol2 = curCol + 1
            if (curRow2 < n and curCol2 < n):
                matrix_copy = [row[:] for row in matrix]
                
                original = matrix_copy[curRow1][curCol1]
                matrix_copy[curRow2][curCol2] = 2
                
                q.append((matrix_copy,newCount, curRow1, curCol2))
                matrix_copy[curRow2][curCol2] = original
            # move left up up
            curRow3 = curRow - 2
            curCol3 = curCol - 1
            if curRow3 > -1 and curCol3 > -1:
              
                matrix_copy = [row[:] for row in matrix]
                original = matrix_copy[curRow3][curCol3]
                matrix_copy[curRow3][curCol3] = 2
                q.append((matrix_copy,newCount, curRow3, curCol3))
                matrix_copy[curRow3][curCol3] = original
            # move left down down
            curRow4 = curRow + 2
            curCol4 = curCol - 1
            if curRow4 < n and curCol4 > -1:
                matrix_copy = [row[:] for row in matrix]
                matrix_copy[curRow4][curCol4] = 2
                q.append((matrix_copy,newCount, curRow4, curCol4))
                
                
                
            # move right right up            
            curRow1 = curRow - 1
            curCol1 = curCol + 2
            
            if (curRow1 > -1 and curCol1 < n):
                
                original = matrix_copy[curRow1][curCol1]
                matrix[curRow1][curCol1] = 2
                q.append((matrix,newCount, curRow1, curCol1))
                matrix_copy[curRow1][curCol1] = original
                
               
                
            # move right right down
            matrix_copy = [row[:] for row in matrix]              
            curRow2 = curRow + 1
            curCol2 = curCol + 2
            if curRow2 < n and curCol2 < n:
                original = matrix_copy[curRow2][curCol2]
                matrix_copy[curRow2][curCol2] = 2
                q.append((matrix_copy,newCount, curRow2, curCol2))
                matrix_copy[curRow2][curCol2] = original
                
            # move left left up
            matrix_copy = [row[:] for row in matrix]
            curRow3 = curRow - 1
            curCol3 = curCol - 2
            if curRow3 > -1 and curCol3 > -1:
                original = matrix_copy[curRow3][curCol3]
                matrix_copy[curRow3][curCol3] = 2
                q.append((matrix_copy,newCount, curRow3, curCol3))
                matrix_copy[curRow3][curCol3] = original
            # move left left down
            curRow4 = curRow + 1
            curCol4 = curCol - 2
            if curRow4 < n and curCol4 > - 1:
                matrix_copy = [row[:] for row in matrix]
                matrix_copy[curRow4][curCol4] = 2
                q.append((matrix_copy,newCount, curRow4, curCol4))
                
        #bishop is not dead. Avoid threatend positions
        else:
            # move right up up
            curRow1 = curRow - 2
            curCol1 = curCol + 1
            if (curRow1 > - 1 and curCol1 < n and matrix[curRow1][curCol1]!=1):
                matrix_copy = [row[:] for row in matrix]
                
                original = matrix_copy[curRow1][curCol1]
                matrix_copy[curRow1][curCol1] = 2
                
                q.append((matrix_copy,newCount, curRow1, curCol1))
                matrix_copy[curRow1][curCol1] = original
            # move right down down
            curRow2 = curRow + 2
            curCol2 = curCol + 1
            if (curRow2 < n and curCol2 < n and matrix[curRow2][curCol2]!=1):
                matrix_copy = [row[:] for row in matrix]
                
                original = matrix_copy[curRow2][curCol2]
                matrix_copy[curRow2][curCol2] = 2
                
                q.append((matrix_copy,newCount, curRow1, curCol2))
                matrix_copy[curRow2][curCol2] = original
            # move left up up
            curRow3 = curRow - 2
            curCol3 = curCol - 1
            if curRow3 > -1 and curCol3 > -1 and matrix[curRow3][curCol3]!=1:
              
                matrix_copy = [row[:] for row in matrix]
                original = matrix_copy[curRow3][curCol3]
                matrix_copy[curRow3][curCol3] = 2
                q.append((matrix_copy,newCount, curRow3, curCol3))
                matrix_copy[curRow3][curCol3] = original
            # move left down down
            curRow4 = curRow + 2
            curCol4 = curCol - 1
            if curRow4 < n and curCol4 > -1 and matrix[curRow4][curCol4]!=1:
                matrix_copy = [row[:] for row in matrix]
                matrix_copy[curRow4][curCol4] = 2
                q.append((matrix_copy,newCount, curRow4, curCol4))
            
                        
            # move right right up 
            curRow1 = curRow - 1
            curCol1 = curCol + 2
            if (curRow1 > - 1 and curCol1 < n and matrix[curRow1][curCol1]!=1):
                matrix_copy = [row[:] for row in matrix]
                
                original = matrix_copy[curRow1][curCol1]
                matrix_copy[curRow1][curCol1] = 2
               
                q.append((matrix_copy,newCount, curRow1, curCol1))
                matrix_copy[curRow1][curCol1] = original
                
               
            # move right right down
            
            curRow2 = curRow + 1
            curCol2 = curCol + 2
            if curRow2 < n and curCol2 < n and matrix[curRow2][curCol2]!=1:
                matrix_copy = [row[:] for row in matrix]
                original = matrix_copy[curRow2][curCol2]
                matrix_copy[curRow2][curCol2] = 2
                q.append((matrix_copy,newCount, curRow2, curCol2))
                matrix_copy[curRow2][curCol2] = original
            # move left left up
            
            curRow3 = curRow - 1
            curCol3 = curCol - 2
            if curRow3 > -1 and curCol3 > -1 and matrix[curRow3][curCol3]!=1:
          
                matrix_copy = [row[:] for row in matrix]
                original = matrix_copy[curRow3][curCol3]
                matrix_copy[curRow3][curCol3] = 2
                q.append((matrix_copy,newCount, curRow3, curCol3))
                matrix_copy[curRow3][curCol3] = original
            # move left left down
            curRow4 = curRow + 1
            curCol4 = curCol - 2
            if curRow4 < n and curCol4 > -1 and matrix[curRow4][curCol4]!=1:
                matrix_copy = [row[:] for row in matrix]
                matrix_copy[curRow4][curCol4] = 2
                q.append((matrix_copy,newCount, curRow4, curCol4))

    
    

moves(6,5,1,0,5,2,3)
# n=3
# board = [ [0 for _ in range(n)] for _ in range(n)]

# print(board)