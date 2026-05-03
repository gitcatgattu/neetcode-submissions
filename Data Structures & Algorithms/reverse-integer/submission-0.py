class Solution:
    def reverse(self, x: int) -> int:
        
        MAX,MIN=2147483647,-2147483648
        res=0
        while x:
            digit=math.fmod(x,10)#-1%10=9 in py 

            x=int(x/10)# -1//10=-1

            if res>int(MAX/10) or (res==MAX and digit>7):
                return 0
            if res<int(MIN/10) or (res==MIN and digit<8):
                return 0
            res=(res*10)+digit
        return int(res)


