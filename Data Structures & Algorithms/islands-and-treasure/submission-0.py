class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visit=set()
        q=deque()
        def addPath(r,c):
            if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or (r,c) in visit or grid[r][c]==-1:
                return
            visit.add((r,c))
            q.append([r,c])
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==0:
                    q.append([r,c])
                    visit.add((r,c))
        curr_dist=0
        while len(q)>0:
            n=len(q)
            for i in range(n):
                r,c=q.popleft()
                grid[r][c]=curr_dist
                addPath(r+1,c)
                addPath(r,c+1)
                addPath(r-1,c)
                addPath(r,c-1)
            curr_dist+=1

