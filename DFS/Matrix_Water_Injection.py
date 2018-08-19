"""
1410. Matrix Water Injection
Given a two-dimensional matrix, the value of each grid represents the height of the terrain. 
The flow of water will only flow up, down, right and left, and it must flow from the high ground 
to the low ground. As the matrix is surrounded by water, it is now filled with water from (R,C) 
and asked if water can flow out of the matrix.

Example
Given

mat =
[
    [10,18,13],
    [9,8,7],
    [1,2,3]
]
R = 1, C = 1, return "YES"。

Explanation:
(1,1) →(1,2)→Outflow.
Given

mat = 
[
    [10,18,13],
    [9,7,8],
    [1,11,3]
]
R = 1, C = 1, return "NO"。

Explanation:
Since (1,1) cannot flow to any other grid, it cannot flow out.
Notice
The input matrix size is n x n, n <= 200.
Ensure that each height is a positive integer.
"""

class Solution:
    """
    @param matrix: the height matrix
    @param R: the row of (R,C)
    @param C: the columns of (R,C)
    @return: Whether the water can flow outside
    """
    def waterInjection(self, matrix, R, C):
        # Write your code here
        m = len(matrix)
        n = len(matrix[0])
        v =  [[False for j in range(0, n)] for i in range(0, m)]
        
        res = self.dfs(matrix, R, C, v)
        
        if res:
            return "YES"
        
        return "NO"
        
    def dfs(self, matrix, R, C, v):
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        
        res = False
        
        for i in range(4):
            nx = R + dx[i]
            ny = C + dy[i]
            if self.outside(matrix, nx, ny):
                return True
            
            
            if not v[nx][ny] and matrix[R][C] > matrix[nx][ny]:
                v[nx][ny] = True
                res = res or self.dfs(matrix, nx, ny, v)
                
        return res
        
        
        
    def outside(self, matrix, R, C):
        m = len(matrix)
        n = len(matrix[0])
        return R < 0 or R >= m or C < 0 or C >= n
        
        
       