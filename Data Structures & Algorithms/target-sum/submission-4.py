class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache={}
        def dfs(i,cursum):
            if (i,cursum) in cache:
                return cache[(i,cursum)] 
            if i>=len(nums):
                return 0
            if i==len(nums)-1:
                if cursum+nums[i]==target and cursum-nums[i]==target:
                    cache[(i,cursum)]=2
                    return 2
                elif (cursum+nums[i]==target or cursum-nums[i]==target):
                    cache[(i,cursum)]=1
                    return 1
            
            cache[(i,cursum)]= dfs(i+1,cursum+nums[i])+dfs(i+1,cursum-nums[i])
            return cache[(i,cursum)]
        return dfs(0,0)
