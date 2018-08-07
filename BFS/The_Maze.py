"""
787. The Maze
There is a ball in a maze with empty spaces and walls. 
The ball can go through empty spaces by rolling up, down, left or right, 
but it won't stop rolling until hitting a wall. When the ball stops, 
it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether 
the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. 
You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

Example
Given:
a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

start coordinate (rowStart, colStart) = (0, 4)
destination coordinate (rowDest, colDest) = (4, 4)

Return:true
Notice
1.There is only one ball and one destination in the maze.
2.Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
3.The given maze does not contain border (like the red rectangle in the example pictures), 
but you could assume the border of the maze are all walls.
5.The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
"""

class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    def hasPath(self, maze, start, destination):
        # write your code here
        m = len(maze)
        n = len(maze[0])
        visited = [ [ False for j in range(n) ] for i in range(m) ]
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        queue = collections.deque()
        queue.append({
            'x': start[0],
            'y': start[1]
        })
        
        while queue:
            size = len(queue)
            for i in range(size):
                entry = queue.popleft()
                curr_x = entry['x']
                curr_y = entry['y']
                visited[curr_x][curr_y] = True
                
                for dir in range(4):
                    curr_x_prime = curr_x
                    curr_y_prime = curr_y
                    nx = curr_x_prime + dx[dir]
                    ny = curr_y_prime + dy[dir]

                    while self.inRange(nx, ny, maze) and maze[nx][ny] == 0:
                        temp_x = nx
                        temp_y = ny
                        nx += dx[dir]
                        ny += dy[dir]
                        curr_x_prime = temp_x
                        curr_y_prime = temp_y
                    
                    if visited[curr_x_prime][curr_y_prime] == False:
                        if curr_x_prime == destination[0] and curr_y_prime == destination[1]:
                            return True
                            
                        queue.append({
                            'x': curr_x_prime,
                            'y': curr_y_prime
                        })
        
        return False
        
        
    def inRange(self, x, y, maze):
        return x >= 0 and x < len(maze) and y >= 0 and y < len(maze[0])