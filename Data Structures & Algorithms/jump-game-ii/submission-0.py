class Solution:
    def jump(self, nums: List[int]) -> int:
        self.res=float('inf')
        def dfs(i,cur):
            if i>=len(nums)-1:
                self.res=min(self.res,cur)
                return True
            for j in range(1,nums[i]+1):
                dfs(i+j,cur+1)
            return False
        dfs(0,0)
        return self.res