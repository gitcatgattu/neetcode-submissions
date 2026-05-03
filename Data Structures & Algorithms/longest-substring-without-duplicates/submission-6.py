class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest,left=0,0
        count=defaultdict(int)
        for right in range(len(s)):
            
            while count[s[right]]>0:
                count[s[left]]-=1
                left+=1
            count[s[right]]+=1
            longest=max(longest,right-left+1)
        return longest