class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        result = 0
        for i in range(len(s)-1):
            if s[i] == 'I' and (s[i+1] == 'V' or s[i+1] == 'X'):
                result -= roman[s[i]]
            elif s[i] == 'X' and (s[i+1] == 'L' or s[i+1] == 'C'):
                result -= roman[s[i]]
            elif s[i] == 'C' and (s[i+1] == 'D' or s[i+1] == 'M'):
                result -= roman[s[i]]
            else:
                result += roman[s[i]]
        result += roman[s[-1]]
        return result
