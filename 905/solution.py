class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        sorted_nums = []
        for num in nums:
            if num % 2 == 0:
                sorted_nums.insert(0, num)
            else:
                sorted_nums.append(num)
        return sorted_nums
        