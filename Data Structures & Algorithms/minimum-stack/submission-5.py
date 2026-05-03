class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self, val: int) -> None:
        self.stack.append((val,min(val,self.stack[-1][1] if self.stack else val)))

    def pop(self) -> None:
        p,q=self.stack.pop()
        return p

    def top(self) -> int:
        s,t=self.stack[-1]
        return s
    def getMin(self) -> int:
        p,q=self.stack[-1]
        return q
        
