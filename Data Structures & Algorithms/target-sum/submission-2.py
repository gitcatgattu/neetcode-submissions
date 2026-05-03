class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        def dfs(i,cursum):
            if i>=len(nums):
                return 0
            if i==len(nums)-1:
                if cursum+nums[i]==target and cursum-nums[i]==target:
                    return 2
                elif (cursum+nums[i]==target or cursum-nums[i]==target):
                    return 1
            
            return dfs(i+1,cursum+nums[i])+dfs(i+1,cursum-nums[i])
        return dfs(0,0)
