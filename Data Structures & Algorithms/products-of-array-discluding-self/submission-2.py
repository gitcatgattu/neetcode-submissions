class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            
        Lp,Rp=1,1
        n=len(nums)
        res=[1]*n
        for i in range(n):
            res[i]*=Lp
            Lp*=nums[i]
        for i in range(n-1,-1,-1):
            res[i]*=Rp
            Rp*=nums[i]
        return res