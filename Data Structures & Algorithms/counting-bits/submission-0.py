class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[0]*(n+1)

        for num in range(n+1):
            i=1
            count=0
            while i<=num:
                if i&num:
                    count+=1
                i*=2
            res[num]=count
        return res