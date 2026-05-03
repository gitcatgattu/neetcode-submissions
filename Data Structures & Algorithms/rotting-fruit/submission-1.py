class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten=set()
        q=deque()
        def addRotten(r,c):
            if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or (r,c) in rotten:
                return
            rotten.add((r,c))
            q.append([r,c])

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==2:
                    rotten.add((r,c))
                    q.append([r,c])
                elif grid[r][c]==0:
                    rotten.add((r,c))
        time=0
        while len(q)>0:
            n=len(q)
            for i in range(n):
                r,c=q.popleft()
                addRotten(r+1,c)
                addRotten(r-1,c)
                addRotten(r,c+1)
                addRotten(r,c-1)
            time+=1
        if len(rotten)!=(len(grid)*len(grid[0])):
            return -1
        if time==0:
            return time
        return time-1