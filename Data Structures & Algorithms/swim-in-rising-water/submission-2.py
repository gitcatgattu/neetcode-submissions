class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        
        minH=[[grid[0][0],0,0]]#
        visit=set((0,0))
        while minH:
            w,r,c=heapq.heappop(minH)
            if r==n-1 and c==n-1:
                return w
            for neiR,neiC in directions:
                nR=neiR+r
                nC=neiC+c
                if nR<0 or nR>=n or nC<0 or nC>=n or (nR,nC) in visit:
                    continue
                heapq.heappush(minH,[max(w,grid[nR][nC]),nR,nC])
                visit.add((nR,nC))
        