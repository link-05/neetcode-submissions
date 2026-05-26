class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buyPrice = prices[0]
        for price in prices:
            if price < buyPrice:
                buyPrice = price
            elif price - buyPrice > maxProfit:
                maxProfit = price - buyPrice
        return maxProfit