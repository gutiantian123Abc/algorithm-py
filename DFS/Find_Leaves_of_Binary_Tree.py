"""
650. Find Leaves of Binary Tree
Given a binary tree, collect a tree's nodes as if you were doing this: 
Collect and remove all leaves, repeat until the tree is empty.

Example
Given binary tree:

    1
   / \
  2   3
 / \     
4   5    
Returns [[4, 5, 3], [2], [1]].

"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    def dfs(self, dic, node):
        if node == None:
            return 0
        
        d = max(self.dfs(dic, node.left), self.dfs(dic, node.right)) + 1
        
        if d not in dic:
            dic[d] = []
        
        dic[d].append(node.val)
        return d
    """
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """
    def findLeaves(self, root):
        # write your code here
        dic = {}
        max_depth = self.dfs(dic, root)
        result = []
        
        for depth in range(1, max_depth + 1):
            result.append(dic[depth])
            
        return result