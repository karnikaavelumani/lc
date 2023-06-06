class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        # Create a word frequency map for each word
        s_map = {}
        for c in s:
            s_map[c] = s_map.get(c, 0) + 1 # initialize to 0 if not found, then increment

        t_map = {}
        for c in t:
            t_map[c] = t_map.get(c, 0) + 1

        return s_map == t_map