from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_profit = 0
        lowest = prices[0]

        for price in prices:
            if price < lowest:
                lowest = price
            elif (price - lowest) > curr_profit:
                curr_profit = price - lowest

        return curr_profit
