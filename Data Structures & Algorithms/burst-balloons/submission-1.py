class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums=[1]+nums+[1]
        dp={}
        def dfs(l,r):
            if l>r:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]
            cur=0
            for i in range(l,r+1):
                coins=nums[l-1]*nums[i]*nums[r+1]
                coins+=dfs(l,i-1)+dfs(i+1,r)
                cur=max(cur,coins)
            dp[(l,r)]=cur
            return cur
        

        return dfs(1,len(nums)-2)