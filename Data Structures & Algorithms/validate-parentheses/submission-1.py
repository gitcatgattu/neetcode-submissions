class Solution:
    def isValid(self, s: str) -> bool:
        
        stack=[]
        for b in s:
            if stack and stack[-1]=="(" and b==")":
                stack.pop()
            elif stack and stack[-1]=="{" and b=="}":
                stack.pop()
            elif stack and stack[-1]=="[" and b=="]":
                stack.pop()
            else:
                stack.append(b)
        return len(stack)==0