class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        water=0
        lB,rB=0,0
        l,r=0,n-1
        while l<r:
            rB=max(rB,height[r])
            lB=max(lB,height[l])
            if lB<=rB:
                water+=max(lB-height[l],0)
                l+=1
                
            else:
                water+=max(0,rB-height[r])
                r-=1
               
        return water

