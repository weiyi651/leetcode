import numpy as np

def lengthOfLIS(self, nums):
    if not nums:
        return 0
    else:
        array_length = len(nums)
        res = np.zeros(shape=(array_length,array_length))
        for i in range(array_length):
            for j in range(i,array_length):
                if nums[i] < nums[j]:
                    res[i][j] = res[i-1][j] + 1
        return res[array_length-1][array_length-1]