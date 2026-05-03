class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dist=set(nums)
        return len(dist)!=len(nums)