class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro=0
        minBuy=prices[0]
        for sellPrice in prices:
            maxPro=max(maxPro,sellPrice-minBuy)
            minBuy=min(minBuy,sellPrice)
        return maxPro