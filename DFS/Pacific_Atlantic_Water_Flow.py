class Solution:
    class ResultType:
        def __init__(self, isPacific, isAtlantic):
            self.isPacific = isPacific
            self.isAtlantic = isAtlantic
            
    def isPacific(self, matrix, i, j):
        return i == -1 or j == -1
        
    def isAtlantic(self, matrix, i, j):
        return i == len(matrix) or j == len(matrix[0])

            
    def dfs(self, matrix, results, visited, both, x, y):
        if both[x][y]:
            return self.ResultType(True, True)
            
        foundPacific = False
        foundAtlantic = False
        
        xDirections = [1, 0, -1, 0]
        yDirections = [0, 1, 0, -1]

        for i in range(0, 4):
            nextX = x + xDirections[i]
            nextY = y + yDirections[i]
            
            if self.isPacific(matrix, nextX, nextY):
                continue
            
            if self.isAtlantic(matrix, nextX, nextY):
                continue
            
            if visited[nextX][nextY]:
                continue
            
            if matrix[nextX][nextY] <= matrix[x][y]:
                visited[nextX][nextY] = True
                result = self.dfs(matrix, results, visited, both, nextX, nextY)
                visited[nextX][nextY] = False
                
                if result.isPacific:
                    foundPacific = True
            
                if result.isAtlantic:
                    foundAtlantic = True
                
        if foundPacific and foundAtlantic:
            both[x][y] = True
            results.append([x,y])
                
            
        return self.ResultType(foundPacific, foundAtlantic)           
                
    """
    @param matrix: the given matrix
    @return: The list of grid coordinates
    """
    def pacificAtlantic(self, matrix):
        # write your code here
        results = []
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return results
        
        visited = [[False] * len(matrix)] * len(matrix[0])
        both = [[False] * len(matrix)] * len(matrix[0])
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                visited[i][j] = True
                result = self.dfs(matrix, results, visited, both, i, j)
                visited[i][j] = False
                
         
                
        return results
            
        
        
        
