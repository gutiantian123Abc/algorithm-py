"""
1442. Order Problem
There is now an order with demand for n items, and the demand for the i-th item is order[i]. 
The factory has m production modes. Each production mode is shaped like [p[1],p[2],...p[n]], 
that is, produce p[1] first items, p[2] second items... You can use multiple production modes. 
Please tell me how many items do not meet the demand at least in the case of not exceeding 
the demand of any kind of items?

Example
Given order=[2,3,1], pattern=[[2,2,0],[0,1,1],[1,1,0]] , return 0.

Explanation:
Use [0,1,1] once, [1,1,0] twice, remaining [0,0,0].
Given order=[2,3,1], pattern=[[2,2,0]] , return 2.

Explanation:
Use [2,2,0] once, remaining [0,1,1].
Notice
1≤n,m≤7
1≤order[i]≤10
0≤pattern[i][j]≤10

时间复杂度 O(n10^m)
"""

class Solution:
    """
    @param order: The order
    @param pattern: The pattern
    @return: Return the number of items do not meet the demand at least
    """
    def getMinRemaining(self, order, pattern):
        # Write your code here
        self.ans = 0
        
        for i in order:
            self.ans += i
            
        self.dfs(order, pattern, 0)
        return self.ans
    
    def dfs(self, order, pattern, id):
        if id == len(pattern):
            res = 0
            for i in order:
                res += i 
            
            self.ans = min(self.ans, res)
            return
        
        maxCnt = 10
        for i in range(len(pattern[id])):
            if pattern[id][i] != 0:
                maxCnt = min(maxCnt, order[i] / pattern[id][i])
                
        for i in range(maxCnt + 1):
            for j in range(len(order)):
                order[j] -= pattern[id][j] * i
                
            self.dfs(order, pattern, id + 1)
            
            for j in range(len(order)):
                order[j] += pattern[id][j] * i