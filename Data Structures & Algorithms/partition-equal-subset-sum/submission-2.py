class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target=sum(nums)
        if target%2!=0:
            return False
        target//=2
        visit=set()
        dp={0:True}
        def dfs(tar):
            if tar in dp:
                return dp[tar]
            if tar<0:
                return False
            for i in range(len(nums)):
                if i not in visit:
                    rem=tar-nums[i]
                    visit.add(i)
                    if dfs(rem):
                        dp[tar]=True
                        return True
                    visit.remove(i)
            dp[tar]=False
            return False
        return dfs(target)
