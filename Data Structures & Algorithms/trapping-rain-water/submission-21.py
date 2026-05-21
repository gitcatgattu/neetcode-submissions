class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        lB,rB=0,0
        water=0
        l,r=0,n-1
        while l<r:
            lB=max(lB,height[l])
            rB=max(rB,height[r])
            if lB<rB:
                water+=lB-height[l]
                l+=1 
            else:
                water+=rB-height[r]
                r-=1
        return water







