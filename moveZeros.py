# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                # 交换后，左指针一定不为0，右指针可能为0
                nums[left], nums[right] = nums[right], nums[left] 
                left += 1
            # 出现一个0，右指针就比左指针多一位，即右指针和左指针的间隔是0的个数
            right += 1