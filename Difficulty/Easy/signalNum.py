## Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

## Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            return reduce(lambda x, y: x ^ y, nums)