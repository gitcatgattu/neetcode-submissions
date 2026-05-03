class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=""
        for ch in s:
            if ch.isalnum():
                st+=ch.lower()
        l=0
        r=len(st)-1
        while l<=r:
            if st[l]!=st[r]:
                return False
            l+=1
            r-=1
        return True
