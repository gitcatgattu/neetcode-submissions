class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        dp={}
        def dfs(i,canBuy):
            if i>=len(prices):
                return 0
            if (i,canBuy) in dp:
                return dp[(i,canBuy)]
            cool=dfs(i+1,canBuy)
            if canBuy:
                buy=dfs(i+1,False)-prices[i]
                dp[(i,canBuy)]=max(buy,cool)
            else:
                sell=dfs(i+2,True)+prices[i]
                dp[(i,canBuy)]=max(sell,cool)
            return dp[(i,canBuy)]
        print(dp)
        return dfs(0,True)