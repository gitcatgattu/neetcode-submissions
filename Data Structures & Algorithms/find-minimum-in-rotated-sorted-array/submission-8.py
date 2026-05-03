class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right=0,len(nums)-1
        ans=nums[0]
        while left<=right:
            mid=(left+right)//2
            if nums[0]<=nums[mid]:#left partition
                left=mid+1
            elif nums[mid]<nums[0]:#right partition
                ans=min(ans,nums[mid])
                right=mid-1
        return ans