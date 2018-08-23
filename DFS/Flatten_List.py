"""
22. Flatten List
Given a list, each element in the list can be a list or integer. 
flatten it into a simply list with integers.

Example
Given [1,2,[1,2]], return [1,2,1,2].

Given [4,[3,[2,[1]]]], return [4,3,2,1].

Challenge
Do it in non-recursive.

Notice
If the element in the given list is a list, it can contain list too.

22. Flatten List
Given a list, each element in the list can be a list or integer. flatten it into a simply list with integers.

Example
Given [1,2,[1,2]], return [1,2,1,2].

Given [4,[3,[2,[1]]]], return [4,3,2,1].

Challenge
Do it in non-recursive.

Notice
If the element in the given list is a list, it can contain list too.
"""

class Solution(object):

    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        res = []
        if isinstance(nestedList, int):
            res.append(nestedList)
            return res
        
        for ele in nestedList:
            if isinstance(ele, int):
                res.append(ele)
            else:
                res.extend(self.flatten(ele))
        return res