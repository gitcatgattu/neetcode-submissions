class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        pre=x
        if n<0:
            for i in range(abs(n-1)):
                x=x/pre
            return x

        if n==0:
            return 1/1


        for i in range(n-1):
            x=x*pre
        return x