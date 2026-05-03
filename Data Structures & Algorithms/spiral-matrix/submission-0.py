class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        m,n=len(matrix),len(matrix[0])
        top,left=0,0
        bottom,right=m-1,n-1

        while top<=bottom and left<=right:
            for i in range(left,right+1):
                res+=matrix[top][i],
            top+=1
            for i in range(top,bottom+1):
                res+=matrix[i][right],
            right-=1
            if top>bottom or left>right:
                continue
            for i in range(right,left-1,-1):
                res+=matrix[bottom][i],
            bottom-=1
            if top>bottom or left>right:
                continue
            for i in range(bottom,top-1,-1):
                res+=matrix[i][left],
            left+=1
        return res