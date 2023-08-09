class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        rules = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []
        for c in s:
            if c in rules:
                stack.append(rules[c])
            elif len(stack) == 0:
                return False
            elif stack[-1] == c:
                stack.pop()
            else:
                return False
        return len(stack) == 0
