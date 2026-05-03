class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n=len(matrix),len(matrix[0])
        
        def dfs(r,c,U,D,L,R):
            if r<0 or c<0 or r>=m or c>=n:
                return
            if matrix[r][c]!=0:
                matrix[r][c]="0"
            if U:
                dfs(r+1,c,U,False,False,False)
            if D:
                dfs(r-1,c,False,D,False,False)
            if L:
                dfs(r,c-1,False,False,L,False)
            if R:
                dfs(r,c+1,False,False,False,R)







        for r in range(m):
            for c in range(n):
                if matrix[r][c]==0:
                    dfs(r,c,True,True,True,True)
