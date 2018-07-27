"""
431. Connected Component in Undirected Graph
Find the number connected component in the undirected graph. 
Each node in the graph contains a label and a list of its neighbors. (a connected component (or just component) of an undirected graph is a subgraph in which any two vertices are connected to each other by paths, and which is connected to no additional vertices in the supergraph.)

Example
Given graph:

A------B  C
 \     |  | 
  \    |  |
   \   |  |
    \  |  |
      D   E
Return {A,B,D}, {C,E}. Since there are two connected component which is {A,B,D}, {C,E}

"""
"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

class Solution:
    """
    @param: nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
    def bfs(self, node, tmp):
        queue = collections.deque()
        queue.append(node)
        self.v[node.label] = True #注意， BFS 若有visited, 一定要在append 的时候update visited , 千万不要在pop出来的时候update visited
        
        while queue:
            size = len(queue)
            for i in range(0, size):
                currnode = queue.popleft()
                tmp.append(currnode.label)
                
                for neighbor in currnode.neighbors:
                    if not self.v[neighbor.label]:
                        queue.append(neighbor)
                        self.v[neighbor.label] = True
                        #注意， BFS 若有visited, 一定要在append 的时候update visited , 千万不要在pop出来的时候update visited

    def connectedSet(self, nodes):
        # write your code here
        result = []
        self.v = {}
        
        for node in nodes:
            self.v[node.label] = False
            
        for node in nodes:
            if not self.v[node.label]:
                tmp = []
                self.bfs(node, tmp)
                result.append(sorted(tmp))
        return result
                
        
            
       
        
