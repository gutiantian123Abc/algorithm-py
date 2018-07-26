"""
First Position of Target
For a given sorted array (ascending order) and a target number, 
find the first index of this number in O(log n) time complexity.

If the target number does not exist in the array, return -1.

Example
If the array is [1, 2, 3, 3, 4, 5, 10], for given target 3, return 2.
"""

class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        left, right = 0, len(nums) - 1
        while left + 1 < right :
            mid = (left + right) / 2
            if target == nums[mid] :
                right = mid
            elif target < nums[mid] :
                right = mid
            else :
                left = mid
                
        if nums[left] == target :
            return left
        elif nums[right] == target :
            return right
        else :
            return -1
