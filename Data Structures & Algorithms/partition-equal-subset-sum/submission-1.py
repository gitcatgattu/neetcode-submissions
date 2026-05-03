class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target=sum(nums)
        if target%2!=0:
            return False
        target//=2
        visit=set()

        def dfs(tar):
            if tar==0:
                return True
            if tar<0:
                return False
            for i in range(len(nums)):
                if i not in visit:
                    rem=tar-nums[i]
                    visit.add(i)
                    if dfs(rem):
                        return True
                    visit.remove(i)
            return False
        return dfs(target)
