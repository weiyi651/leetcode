class Solution:

    @staticmethod
    def max_sum(nums):
        num_list_len = len(nums)
        m = [0,0] + [0] *num_list_len
        for i in range(0, num_list_len):
            m[i+2] = max(m[i] + nums[i], m[i+1])
        return m[-1]

    def rob(self, nums: List[int]) -> int:
        num_list_len = len(nums)
        if num_list_len == 1:
            return nums[0]
        elif num_list_len == 2:
            return max(nums)
        elif num_list_len >=3:
            return max(self.max_sum(nums[:-1]), self.max_sum(nums[1:]))