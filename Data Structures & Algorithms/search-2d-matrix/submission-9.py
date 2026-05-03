class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        s,e=0,m*n-1
        while s<=e:
            mid=s+(e-s)//2
            midValue=matrix[mid//n][mid%n]
            if midValue==target:
                return True
            elif midValue<target:
                s=mid+1
            else:
                e=mid-1






        return False

