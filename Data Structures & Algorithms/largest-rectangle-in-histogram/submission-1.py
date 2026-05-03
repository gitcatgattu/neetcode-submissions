class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        n=len(heights)
        maxarea=0
        for i in range(1+n):
            while stack and (i==n or heights[i]<=heights[stack[-1]]):
                h=heights[stack.pop()]
                w=i if not stack else i-stack[-1]-1
                maxarea=max(maxarea,h*w)
            stack.append(i)
        return maxarea
