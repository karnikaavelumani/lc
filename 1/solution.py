class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) == 2:
            return [0, 1]
        hm = {}
        for i, num in enumerate(nums): # returns iterator of tuples
            if num in hm:
                return [hm[num], i]
            
            # return target - num
            hm[target - num] = i

# iteration 1
# hm = {
#     3: 0,
# }
# i = 0
# num = 3

# iteration 2
# hm = {
#     3: 0, 4: 1
# }
# i = 1
# num = 2