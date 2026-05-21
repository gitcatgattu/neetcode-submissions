class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        maxArea=0
        while l<r:
            h=min(heights[l],heights[r])
            w=r-l
            curArea=h*w
            maxArea=max(curArea,maxArea)
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return maxArea