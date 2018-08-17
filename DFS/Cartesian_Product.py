"""
935. Cartesian Product
We use a two-dimensional array setList[][] to represent a collection array, 
and each element in setList[i] is an integer and is not the same. 
Find the cartesian product of setList[0],setList[1],...,setList[setList.length - 1].
In general, the Cartesian product of the collection A and the set B is A×B = {(x,y)|x∈A∧y∈B}。

Example
Given setList = [[1,2,3],[4],[5,6]], return [[1,4,5],[1,4,6],[2,4,5],[2,4,6],[3,4,5],[3,4,6]],

Explanation:
The cartesian product of [1,2,3], [4] and [5,6] is [[1,4,5],[1,4,6],[2,4,5],[2,4,6],[3,4,5],[3,4,6]].
Given setList = [[1,2,3],[4]] , return [[1,4],[2,4],[3,4]]。

Explanation:
The cartesian product of [1,2,3] and [4] is [[1,4],[2,4],[3,4]].
Notice
1 <= setList.length <= 5
1 <= setList[i].length <= 5
"""

class Solution:
    """
    @param setList: The input set list
    @return: the cartesian product of the set list
    """
    def getSet(self, setList):
        # Write your code here
        ans = []
        List = []
        self.dfs(ans, 0, setList, List)
        return ans
        
    def dfs(self, ans, pos, setList, List):
        import copy
        if pos == len(setList):
            ans.append(copy.deepcopy(List))
            return
        
        for i in setList[pos]:
            List.append(i)
            self.dfs(ans, pos + 1, setList, List)
            List.pop()