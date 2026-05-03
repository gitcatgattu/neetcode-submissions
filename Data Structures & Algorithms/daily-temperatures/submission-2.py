class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        res=[0]*n
        stack=[]#temp ,idx
        for i in range(n):
            while stack and stack[-1][0]<temperatures[i]:
                t,idx=stack.pop()
                res[idx]=i-idx
            stack.append((temperatures[i],i))
        return res
            
