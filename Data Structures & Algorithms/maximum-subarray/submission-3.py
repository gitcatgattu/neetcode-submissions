class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp=0
       
        res=min(nums)
        for r in range(len(nums)):
            temp+=nums[r]


            res=max(res,temp)
            temp=max(0,temp)

        return res

                                                       