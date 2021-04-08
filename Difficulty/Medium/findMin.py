# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# v1 遍历 O(n)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                pass
            else:
                return nums[i+1]
        return nums[0]

# v2 二分查找 O(logn)
class Solution:
    def findMin(self, nums: List[int]) -> int:    
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if nums[pivot] < nums[high]:
                high = pivot 
            else:
                low = pivot + 1
        return nums[low]