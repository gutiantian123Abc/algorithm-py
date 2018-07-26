"""
Search a 2D Matrix
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example
Consider the following matrix:

[
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
Given target = 3, return true.

Challenge
O(log(n) + log(m)) time
"""

class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if len(matrix) == 0 :
            return False
            
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m - 1 
        
        while start + 1 < end :
            mid = start + (end - start) / 2
            if matrix[mid][0] == target:
                return True
            elif target < matrix[mid][0] :
                end = mid
            else :
                start = mid
                
                
        row = 0
        
        if matrix[start][0] <= target and matrix[start][n - 1] >= target :
            row = start
        elif matrix[end][0] <= target and matrix[end][n - 1] >= target :
            row = end
        else :
            return False

        left, right = 0, n - 1
        while left + 1 < right :
            mid = left + (right - left) / 2
            if matrix[row][mid] == target :
                return True
            elif target < matrix[row][mid] :
                right = mid
            else :
                left = mid
                
        if matrix[row][left] == target or matrix[row][right] == target :
            return True
            
        return False
        