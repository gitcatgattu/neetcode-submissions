class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        track=set()
        l=0
        n=len(s)
        dups=0
        ans=0
        for r in range(n):
            while s[r] in track:
                track.remove(s[l])
                l+=1
            track.add(s[r])
            ans=max(ans,r-l+1)
        return ans


            