"""
628. Maximum Subtree
Given a binary tree, find the subtree with maximum sum. 
Return the root of the subtree.

Example
Given a binary tree:

     1
   /   \
 -5     2
 / \   /  \
0   3 -4  -5 
return the node with value 3.

"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    class resultType:
        def __init__(self, maxNode, maxSum, sum):
            self.maxNode = maxNode
            self.sum = sum
            self.maxSum = maxSum
            
    def dfs(self, root):
        if root is None:
            return self.resultType(None, float('-inf'), 0)
            
        right = self.dfs(root.right)
        left = self.dfs(root.left)
        
        currSum = root.val + right.sum + left.sum
        
        if currSum > right.maxSum and currSum > left.maxSum:
            return self.resultType(root, currSum, currSum)
        else:
            if right.maxSum > left.maxSum:
                return self.resultType(right.maxNode, right.maxSum, currSum)
            else:
                return self.resultType(left.maxNode, left.maxSum, currSum)
        
    """
    @param root: the root of binary tree
    @return: the maximum weight node
    """
    def findSubtree(self, root):
        # write your code here
        if not root or root.left is None and root.right is None:
            return root
            
        resulttype = self.dfs(root)
        return resulttype.maxNode