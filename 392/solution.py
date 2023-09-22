class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) is 0:
            return True

        curr_index = 0
        for i in range(len(t)):
            if t[i] is s[curr_index]:
                curr_index += 1
            if curr_index is len(s):
                return True
        return False
        