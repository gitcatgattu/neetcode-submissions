class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            
        Lp,Rp=1,1
        n=len(nums)
        res=[1]*n


        for i in range(n):
            
            res[i]*=Lp
            res[n-i-1]*=Rp
            Lp*=nums[i]
            Rp*=nums[n-i-1]
        return res
        