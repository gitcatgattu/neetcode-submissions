class Solution:
    def trap(self, height: List[int]) -> int:
        area=0

        l,r=0,len(height)-1
        maxL,maxR=height[l],height[r]

        while l<r:
            if height[l]<height[r]:
                l+=1
                if maxL-height[l]>0:
                    area+=maxL-height[l]
                maxL=max(maxL,height[l])
            else:
                r-=1
                if maxR-height[r]>0:
                    area+=maxR-height[r]
                maxR=max(maxR,height[r])
        return area