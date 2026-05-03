class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        rob=[0]*n
        one=nums[n-2]
        two=nums[n-1]

        for i in range(n-3,-1,-1):
            temp=one
            one=max(one,nums[i]+two)
            two=temp
        return max(one,two)