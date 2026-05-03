class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        res=0
        for i in nums:
            if i-1 not in numset:
                length=1
                while i+1 in numset:
                    length+=1
                    i+=1
                res=max(length,res)
        return res