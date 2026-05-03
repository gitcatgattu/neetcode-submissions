class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count=[0]*26
        for c in s1:
            s1Count[ord(c)-ord('a')]+=1
        s2Count=[0]*26
        l=0
        for r in range(len(s2)):
            s2Count[ord(s2[r])-ord('a')]+=1
            if r-l+1<len(s1):
                continue
            if s1Count==s2Count:
                return True
            # if "".join(str(c)+"#" for c in s1Count)=="".join(str(c)+"#" for c in s2Count):
            #     return True
            s2Count[ord(s2[l])-ord('a')]-=1
            l+=1
        return False