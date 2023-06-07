class Solution(object):
    def lengthOfLastWord(self, s):
        txt = s.split() # ["Hello", "World"]
        return len(txt[-1])