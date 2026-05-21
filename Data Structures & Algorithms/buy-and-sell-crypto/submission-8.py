class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        maxP=0
        minPrice=[float('inf')]*n
        for i in range(1,n):
            minPrice[i]=min(minPrice[i-1],prices[i-1])
        for j in range(n-1,-1,-1):
            maxP=max(maxP,prices[j]-minPrice[j])
        '''for i in range(n):
            buy=prices[i]
            for j in range(i+1,n):
                sell=prices[j]
                profit=sell-buy
                maxP=max(maxP,profit)*/'''
        return maxP
