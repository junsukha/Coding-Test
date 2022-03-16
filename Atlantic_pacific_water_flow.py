# Steps = [   
#         [-1,0], # Up
#         [0,1],  # Right
#         [1,0], # bottom
#         [0,-1] # Left
#     ]
 
# def withinLimits(row_num, col_num, total_rows, total_cols):
#     if 0 <= row_num < total_rows and 0 <= col_num < total_cols:
#         return True
#     return False
 
 
# def waterSlope(oceanMatrix, matrix, row, col):
#     nrows, ncols = len(matrix), len(matrix[0])
#     for i in Steps:
#         if withinLimits(row+i[0], col+i[1], nrows, ncols):
#             if matrix[row+i[0]][col+i[1]] >= matrix[row][col] and not oceanMatrix[row+i[0]][col+i[1]]:
#                 oceanMatrix[row+i[0]][col+i[1]] = True
#                 waterSlope(oceanMatrix, matrix, row+i[0], col+i[1])
 
# def commonWaterFlow(matrix):
#     matrix_rows = len(matrix)
#     matrix_cols = len(matrix[0])
#     pacificMatrix = [[False for _ in range(matrix_cols)] for _ in range(matrix_rows)]
#     atlanticMatrix = [[False for _ in range(matrix_cols)] for _ in range(matrix_rows)]
     
#     pacificMatrix[0][1] = True
#     pacificMatrix[0][2] = True
     
#     for i in range(matrix_cols):
#         pacificMatrix[0][i] = True
#         atlanticMatrix[matrix_rows-1][i] = True
     
#     for i in range(matrix_rows):
#         pacificMatrix[i][0] = True
#         atlanticMatrix[i][matrix_cols-1] = True
     
#     for i in range(matrix_cols):
#         waterSlope(pacificMatrix, matrix, 0, i)
#         waterSlope(atlanticMatrix, matrix, matrix_rows-1, i)
     
#     for i in range(matrix_rows):
#         waterSlope(pacificMatrix, matrix, i, 0)
#         waterSlope(atlanticMatrix, matrix, i, matrix_cols-1)
     
#     Count = 0
     
#     for i in range(matrix_rows):
#         for j in range(matrix_cols):
#             if pacificMatrix[i][j] and atlanticMatrix[i][j]:
#                 Count += 1
     
#     return Count
 
# mat = [ [ 1, 2, 2, 3, 5 ],  # T-T-T-T-T     F-F-F-F-T
#         [ 3, 2, 3, 4, 4 ],  # T-T-T-T-T     F-F-F-T-T
#         [ 2, 4, 5, 3, 1 ],  # T-T-T-F-F     F-F-T-T-T
#         [ 6, 7, 1, 4, 5 ],  # T-T-F-F-F     T-T-T-T-T
#         [ 5, 1, 1, 2, 4 ] ] # T-F-F-F-F     T-T-T-T-T
# print(commonWaterFlow(mat))


pacific, atlantic = 1, 2

class Solution(object):
    
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        
        
        res = []
        visited = [[0 for _ in range(len(heights[0]))] for _ in range(len(heights))]
        
        for row in range(len(heights)):
            self.helper(heights, row, 0, float('-inf'), pacific, visited, res )
            self.helper(heights, row, len(heights[0])-1, float('-inf'), atlantic, visited, res)
            
        for col in range(len(heights[0])):
            self.helper(heights, 0, col, float('-inf'), pacific, visited, res)
            self.helper(heights, len(heights)-1, col, float('-inf'), atlantic, visited, res)
            
        return res
    def helper(self, matrix, i , j, prev_height, prev_value, visited, res):
        if i >= 0 and i < len(matrix) \
            and j >= 0 and j < len(matrix[0]):
                if (visited[i][j] | prev_value) == visited[i][j] \
                    or matrix[i][j] < prev_height:
                        return
        
                visited[i][j] |= prev_value
                if visited[i][j] == (pacific | atlantic):
                    res.append([i,j])
                    
                
                direc = [[0,1],[0,-1],[1,0],[-1,0]]
                for x,y in direc:
                    self.helper(matrix, i+x, j+y, matrix[i][j], prev_value, visited, res)
            
        