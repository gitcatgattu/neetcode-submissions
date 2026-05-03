class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack=[]
        
        for i in tokens:
            
            if i=="+" or i=="-" or i=="*" or i=="/":
                b=stack.pop()
                a=stack.pop()
                if i=="+":
                    res=a+b
                elif i=="-":
                    res=a-b
                elif i=="*":
                    res=a*b
                else:
                    res=int(a/b)
                stack.append(res)
            else:
                stack.append(int(i))
            print(stack)
        return stack[0]