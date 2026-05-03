class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,ans=0,0
        maxarea=0
        r=len(heights)-1
        while l<r:

            height=min(heights[l],heights[r])
            width=r-l
            area=height*width
            maxarea=max(maxarea,area)

            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return maxarea
