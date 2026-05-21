class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        res=0
        for i in numset:
            if i-1 not in numset:
                l=1
                while i+1 in numset:
                    i+=1
                    l+=1
                res=max(res,l)
        return res
