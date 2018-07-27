"""
120. Word Ladder
Given two words (start and end), and a dictionary,
 find the length of shortest transformation sequence from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
Example
Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
"""

class Solution:
    def nextWords(self, word, visited, dict):
        nextwords = set()
        for i in range(0, len(word)):
            part1 = word[:i]
            part2 = word[i + 1:]
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] != c:
                    nextWord = part1 + c + part2
                    if nextWord not in visited and nextWord in dict:
                        nextwords.add(nextWord)
                        
        return nextwords
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        queue = collections.deque()
        queue.append(start)
        visited = set()
        dict.add(end)
        
        length = 1
        while queue:
            size = len(queue)
            for i in range(0, size):
                word = queue.popleft()
                if word == end:
                    return length
                else:
                    nextwords = set()
                    nextwords = self.nextWords(word, visited, dict)
                    for nextword in nextwords:
                        queue.append(nextword)
                        visited.add(nextword)
            length = length + 1
            
        return  0