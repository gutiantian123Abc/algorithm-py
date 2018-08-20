"""
1386. Cable Car Ride
When Xiao Jiu came to a place to ride a cable car, he could only ride a cable car once, 
so he wanted to extend the cable car as much as possible. It is known that the cable car 
station distribution can be seen as an n x m matrix, each grid point representing the height 
of the cable car station. He can start a cable car from any station. The cable car can only 
move from a low altitude to a high altitude, taking 1unit of time. The cable car can move in 
eight directions. (up and down, left, right, top left, top right, bottom left, bottom right). 

Q. How long can Xiao Jiu ride the cable car?

Example
Given mat =

[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
return 7.

Explanation:
1→2→3→5→7→8→9 This route is the longest.
Given mat =

[
    [1,2,3],
    [6,5,4],
    [7,8,9]
]
return 9.

Explanation:
1→2→3→4→5→6→7→8→9 This route is the longest.
Notice
1 <= n, m <= 20。
The height of the cable car station entered does not exceed 100000.

"""

class Solution:
    """
    @param height: the Cable car station height
    @return: the longest time that he can ride
    """
    def cableCarRide(self, height):
        # Write your code here
        self.m = len(height)
        self.n = len(height[0])
        self.dx = [1, -1, 0, 0, 1, -1, -1, 1]
        self.dy = [0, 0, 1, -1, 1, 1, -1, -1]
        self.std_matrix = [[0 for j in range(self.n)] for i in range(self.m)]
        self.maxVal = 0
        
        for i in range(self.m):
            for j in range(self.n):
                self.dfs(i, j, height)

        return self.maxVal
        
    def dfs(self, i, j, height):
        maxLen = self.std_matrix[i][j]
        check = True
        for direct in range(8):
            nx = i + self.dx[direct]
            ny = j + self.dy[direct]
 
            if self.inBound(nx, ny) and height[i][j] < height[nx][ny]:
                check = False
                if self.std_matrix[nx][ny] > 0:
                    maxLen = max(maxLen, self.std_matrix[nx][ny] + 1)
                else:
                    maxLen = max(maxLen, self.dfs(nx, ny, height) + 1)
    
        if check:
            self.std_matrix[i][j] = 1
            return 1
        else:
            self.maxVal = max(self.maxVal, maxLen)
            return maxLen
                
    def inBound(self, x, y):
        return x >= 0 and x < self.m and y >= 0 and y < self.n