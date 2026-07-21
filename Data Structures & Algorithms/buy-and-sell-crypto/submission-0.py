class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        highestProfit = 0
        for i in range(length):
            for k in range(i+1, length):
                highestProfit = max(highestProfit, prices[k]-prices[i])

        return highestProfit