class Solution:
    def hammingWeight(self, n: int) -> int:
        

        count=0
        i=1
        while i<=n:
            if i&n:
                count+=1
            i=i*2
        return count