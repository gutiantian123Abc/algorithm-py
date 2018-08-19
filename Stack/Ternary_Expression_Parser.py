"""
887. Ternary Expression Parser
Given a string representing arbitrarily nested ternary expressions, 
calculate the result of the expression. 
You can always assume that the given expression is valid and only consists of 
digits 0-9, ?, :, T and F (T and F represent True and False respectively).

Example
Given expression = "T?2:3", return "2".

Explanation: 
If true, then result is 2; otherwise result is 3.
Given expression = "F?1:T?4:5", return "4".

Explanation: 
The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:

             "(F ? 1 : (T ? 4 : 5))"                   "(F ? 1 : (T ? 4 : 5))"
          -> "(F ? 1 : 4)"                 or       -> "(T ? 4 : 5)"
          -> "4"                                    -> "4"
Given expression = "T?T?F:5:3", return "F".

Explanation: 
The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:

             "(T ? (T ? F : 5) : 3)"                   "(T ? (T ? F : 5) : 3)"
          -> "(T ? F : 3)"                 or       -> "(T ? F : 5)"
          -> "F"                                    -> "F"
Notice
The length of the given string is ≤ 10000.
Each number will contain only one digit.
The conditional expressions group right-to-left (as usual in most languages).
The condition will always be either T or F. That is, the condition will never be a digit.
The result of the expression will always evaluate to either a digit 0-9, T or F.
"""

class Solution:
    """
    @param expression: a string, denote the ternary expression
    @return: a string
    """
    def parseTernary(self, expression):
        # write your code here
        qStack = collections.deque()
        words = []
        counter = 0
        for c in expression:
            if c == '?':
                qStack.append(counter)
                
            words.append(c)
            counter += 1
        
        while qStack:
            q_index = qStack.pop()
            condition_index = q_index - 1
            firstpart_index = q_index + 1
            secondpart_index = q_index + 3
            
            res = self.cal(words, condition_index, firstpart_index, secondpart_index)
            
            for index in range(secondpart_index, condition_index - 1, -1):
                words.pop(index)
                
            words.insert(condition_index, res)
            
        return words[0]
        
    def cal(self, words, condition_index, firstpart_index, secondpart_index):
        if words[condition_index] == 'T':
            return words[firstpart_index]
        else:
            return words[secondpart_index]