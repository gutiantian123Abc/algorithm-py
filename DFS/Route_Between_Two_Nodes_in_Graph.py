"""
176. Route Between Two Nodes in Graph
Given a directed graph, design an algorithm to find out whether 
there is a route between two nodes.

Example
Given graph:

A----->B----->C
 \     |
  \    |
   \   |
    \  v
     ->D----->E
for s = B and t = E, return true

for s = D and t = C, return false
"""

"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    def dfs(self, node, visited, t):
        if node == t:
            return True
        
        visited.add(node)
        for neighbor in node.neighbors:
            if neighbor not in visited:
                if self.dfs(neighbor, visited, t):
                    return True
        
        return False
    
    """
    @param: graph: A list of Directed graph node
    @param: s: the starting Directed graph node
    @param: t: the terminal Directed graph node
    @return: a boolean value
    """
    def hasRoute(self, graph, s, t):
        # write your code here
        if s not in graph or t not in graph:
            return False
            
        if s == t:
            return True
            
        visited = set()
        return self.dfs(s, visited, t)