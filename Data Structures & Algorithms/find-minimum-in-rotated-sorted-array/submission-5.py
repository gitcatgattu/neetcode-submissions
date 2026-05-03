class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        l,r=0,n-1
        res=r
        while l<=r:
            mid=(l+r)//2
            inLeft=True if nums[mid]>nums[-1] else False
            if inLeft:
                l=mid+1

            else:
                res=mid
                r=mid-1
        return nums[res]
