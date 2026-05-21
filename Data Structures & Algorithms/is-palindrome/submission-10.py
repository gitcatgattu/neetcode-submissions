class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS=[]
        for i in s:
            if i.isalnum():
                newS.append(i.lower())
        newSt="".join(newS)
        l,r=0,len(newSt)-1
        while l<r:
            if newSt[l]!=newSt[r]:
                return False
            l+=1
            r-=1
        return True