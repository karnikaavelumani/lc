class Solution(object):
    def getConcatenation(self, nums):
        copy = []
        counter = 0
        for elem in nums:
            copy.append(elem)
        
        copy.extend(nums)
        return copy
