class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=collections.defaultdict(int)
        for i in range(len(nums)):
            n=nums[i]
            if target-n in d:
                return [d[target-n],i]
            d[n]=i