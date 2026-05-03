class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        self.length=0
        visit=set()
        def dfs(r,c,curlen):
            visit.add((r,c))
            self.length=max(self.length,curlen)
            
            dirs=[[0,1],[1,0],[-1,0],[0,-1]]
            for R,C in dirs:
                row=R+r
                col=C+c
                if row<0 or col<0 or row>=len(matrix) or col>=len(matrix[0]) or matrix[row][col]<=matrix[r][c]:
                    continue
                dfs(row,col,curlen+1)
            visit.remove((r,c))

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i,j,0)
        return self.length+1
