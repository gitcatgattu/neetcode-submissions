class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def dfs(i):
            if i>=len(nums)-1:
                print(i)

                return True
            for j in range(1,1+nums[i]):
                if dfs(j+i):
                    print(j+i)
                    return True
            return False
        return dfs(0)