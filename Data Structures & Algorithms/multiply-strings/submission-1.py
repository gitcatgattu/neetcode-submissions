class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1,num2]:
            return "0"
        m,n=len(num1),len(num2)
        num1,num2=num1[::-1],num2[::-1]
        res=[0]*(m+n)

        for i1 in range(m):
            for i2 in range(n):
                digit=int(num1[i1])*int(num2[i2])

                res[i1+i2]+=digit%10
                carry=res[i1+i2]//10
                res[i1+i2]=res[i1+i2]%10
                res[i1+i2+1]+=digit//10+carry


        res,b=res[::-1],0
        while b<len(res) and res[b]==0:
            b+=1

        return "".join([str(i) for i in res[b:]])


