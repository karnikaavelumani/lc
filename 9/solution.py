class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        lst = list(str(x))
        temp = list(reversed(lst))
        
        if x < 0:
            return False
        elif lst == temp:
            return True