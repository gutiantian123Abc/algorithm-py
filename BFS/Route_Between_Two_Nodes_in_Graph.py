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
        queue = collections.deque()
        queue.append(s)
        visited.add(s)
        #注意， BFS 若有visited, 一定要在append 的时候update visited , 千万不要在pop出来的时候update visited
        
        while queue:
            size = len(queue)
            for i in range(0, size):
                currnode = queue.popleft()
                if currnode == t:
                    return True
                
                for node in currnode.neighbors:
                    if node not in visited:
                        queue.append(node)
                        visited.add(node)#注意， BFS 若有visited, 一定要在append 的时候update visited , 千万不要在pop出来的时候update visited
                        
        return False