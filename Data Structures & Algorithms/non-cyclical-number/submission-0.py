class Solution:
    def isHappy(self, n: int) -> bool:
        
        def diSum(num):
            curSum=0
            for d in str(num):
                d=int(d)
                d2=d*d
                curSum+=d2
            return curSum
        

        seen=set([n])
        while True:
            if n==1:
                return True
            n=diSum(n)
            if n in seen:
                return False
            else:
                seen.add(n)

