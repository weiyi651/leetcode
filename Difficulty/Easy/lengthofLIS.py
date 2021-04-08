# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# A subsequence is a sequence that can be derived from an array
# by deleting some or no elements without changing the order of the remaining elements. 
# For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
import numpy as np
from typing import List

def lengthOfLIS(nums:List[int]) -> int:
    if not nums:
        return 0
    else:
        array_length = len(nums)
        res = np.zeros(shape=(array_length,array_length))
        for i in range(array_length):
            for j in range(i,array_length):
                if nums[i] < nums[j]:
                    res[i][j] = res[i-1][j] + 1
                    # print("***********************")
                    # print(nums[i],nums[j],res[i][j])
            print("***********************")
            print(res)
        return (int(res[array_length-1][array_length-1]) + 1)

if __name__ == '__main__':
    nums = [10,9,2,5,3,7,101,18]
    print(lengthOfLIS(nums))