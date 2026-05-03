class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        res=0
        for n in nums:
            if n-1 not in nums:
                cur=1
                num=n
                while num+1 in nums:
                    cur+=1
                    num+=1

                res=max(res,cur)
        return res
