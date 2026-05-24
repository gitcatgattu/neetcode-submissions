class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        lB,rB=0,0
        l,r=0,n-1
        water=0
        while l<r:
            lB=max(lB,height[l])
            rB=max(rB,height[r])
            if lB<=rB:
                water+=max(0,lB-height[l])
                l+=1
            else:
                water+=max(0,rB-height[r])
                r-=1
        return water
