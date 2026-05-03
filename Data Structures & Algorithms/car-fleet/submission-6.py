class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n=len(position)
        pairs=[(position[i],speed[i]) for i in range(n)]
        pairs.sort()
        stack=[]

        for i in range(n-1,-1,-1):
            pos,v=pairs[i]
            time=(target-pos)/v
            if stack and stack[-1]>=time:
                continue
            else:
                stack.append(time)
        return len(stack)
