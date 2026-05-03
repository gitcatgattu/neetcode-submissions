import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charArr=[0]*26
        if len(s)!=len(t):
            return False
        for i in range(len(s)):

            charArr[ord(s[i])-ord('a')]+=1
            charArr[ord(t[i])-ord('a')]-=1
        for i in charArr:
            if i!=0:
                return False
        return True
        
