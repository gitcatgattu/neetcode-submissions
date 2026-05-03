class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        rotated=[[0]* n for i in range(n)]
        for r in range(n):
            for c in range(n):
                rotated[c][n-1-r]=matrix[r][c]
        
        # for i in range(n//2):
        #     matrix[i],matrix[n-1-i]=matrix[n-1-i],matrix[i]
        for i in range(n):
            for j in range(n):
                matrix[i][j]=rotated[i][j]
