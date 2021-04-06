from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = float("inf")
        current_max_profit = -float("inf")
        for i in prices:
            if i < min_val:
                min_val = i
            current_max_profit = max(current_max_profit, i - min_val)
        if current_max_profit < 0:
            current_max_profit = 0
        return current_max_profit


if __name__ == "__main__":
    print(Solution.maxProfit(Solution(), [1, 2, 3, 4]))