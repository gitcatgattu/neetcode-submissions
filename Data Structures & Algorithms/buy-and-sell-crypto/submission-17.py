class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice=prices[0]
        maxprofit=0
        n=len(prices)
        
        
        sell=prices[n-1]
        maxprofit=0
        for i in range(n-2,-1,-1):
            cur=sell-prices[i]
            maxprofit=max(maxprofit,cur)
            sell=max(sell,prices[i])
        return maxprofit
        
        '''n=len(prices)
        buy=prices[0]
        maxP=0

        for i in range(1,n):
            cur=prices[i]-buy
            maxP=max(maxP,cur)
            buy=min(buy,prices[i])
        return maxP
        
        
        
        
        
        
        '''
        