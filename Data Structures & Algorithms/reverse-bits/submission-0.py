class Solution:
    def reverseBits(self, n: int) -> int:
        

        res=["0"]*32

        i=1
        idx=0
        while i<=n:
            if i&n:
                res[idx]="1"
            i*=2
            idx+=1

        s="".join(res)
        return int(s,2)

