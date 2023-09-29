class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_ascending = None
        prev_num = None
        for i in range(len(nums)):
            curr_num = nums[i]
            if prev_num is not None and is_ascending is None:
                if curr_num is not prev_num:
                    is_ascending = curr_num > prev_num
            if is_ascending is not None:
                if (is_ascending and prev_num > curr_num) or (not is_ascending and prev_num < curr_num):
                    return False
            prev_num = curr_num
        return True
