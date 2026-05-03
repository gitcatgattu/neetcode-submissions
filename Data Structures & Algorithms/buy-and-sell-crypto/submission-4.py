class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        profit=0
        #first draw a chart of time vs prices connect down to up with green line and
        #up to down with red line

        for r in range(1,len(prices)):
            

            if prices[r]-prices[l]>profit:
                profit=max(prices[r]-prices[l],profit)
            if prices[r]<prices[l]:
                l=r
        return profit