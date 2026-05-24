class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars=[0]*26
        n=len(s)
        ans=0
        l=0
        for r in range(n):
            chars[ord(s[r])-65]+=1
            
            while (r-l+1)-max(chars)>k:
                chars[ord(s[l])-65]-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans



            
