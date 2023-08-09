class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        # i = 0, nums = [0,0,1], count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                moveZero(nums, i, count)
                count += 1

def moveZero(nums: List[int], zero_index: int, seen_zeroes: int) -> None:
    # Starting from zero_index, swap the item until you reach index = len(nums)-seen_zeroes.
    for i in range(zero_index, len(nums) - seen_zeroes - 1):
        swap(nums, i, i+1)


def swap(nums: List[int], i: int, j: int) -> None:
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp