"""
Binary Tree Level Order Traversal
Given a binary tree, return the level order traversal of its nodes' values. 
(ie, from left to right, level by level).

Example
Given binary tree {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7
 

return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]
Challenge
Challenge 1: Using only 1 queue to implement it.

Challenge 2: Use DFS algorithm to do it.

"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        results = []
        if not root :
            return results
        queue = collections.deque()
        queue.append(root)
        while queue:
            size = len(queue)
            new_q = []
            for i in range(0, size):
                node = queue.popleft()
                new_q.append(node.val)
                if node.left:
                   queue.append(node.left) 
                if node.right:
                    queue.append(node.right)
            results.append(new_q)       
            
        return results
        
                    
                
                
                
            
            
            
            
            
            
            
            
            
            

