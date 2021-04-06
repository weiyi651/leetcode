from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        repeat_dict = {}
        majorityElement = None
        majorityNum = 0
        for i in nums:
            if i not in repeat_dict:
                repeat_dict[i] = 1
            else:
                repeat_dict[i] +=1
            if repeat_dict[i] > majorityNum:
                majorityElement = i
                majorityNum = repeat_dict[i]
        return majorityElement