"""
726. Check Full Binary Tree
A full binary tree is defined as a binary tree in which all nodes have 
either zero or two child nodes. Conversely, there is no node in a full binary tree,
 which has one child node. More information about full binary trees can be found here.

Full Binary Tree
      1
     / \
    2   3
   / \
  4   5

Not a Full Binary Tree
      1
     / \
    2   3
   / 
  4   
Example
Given tree {1,2,3}, return true
Given tree {1,2,3,4}, return false
Given tree {1,2,3,4,5} return true
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
    @param root: the given tree
    @return: Whether it is a full tree
    """
    def isFullTree(self, root):
        # write your code here
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            size = len(queue)
            for i in range(0, size):
                node = queue.popleft()
                if node.left and node.right:
                    queue.append(node.left)
                    queue.append(node.right)
                elif node.left:
                    return False
                elif node.right:
                    return False
                else:
                    continue
        return True