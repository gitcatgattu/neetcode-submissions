class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        l=0
        lB=[0]*n
        for i in range(1,n):
            lB[i]=max(lB[i-1],height[i-1])
        r=0
        rB=[0]*n
        for i in range(n-2,-1,-1):
            rB[i]=max(rB[i+1],height[i+1])

        water=0
        for i in range(n):
            water+=max(min(lB[i],rB[i])-height[i],0)
        return water



