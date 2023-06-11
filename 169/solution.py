from collections import defaultdict

class Solution(object):
    def majorityElement(self, nums):
        freq_map = defaultdict(int)
        record_highest_n = -1
        for n in nums:
            freq_map[n]+=1 # if n does not exist, set to 0
            if freq_map[n] > freq_map[record_highest_n]:
                record_highest_n=n
        return record_highest_n