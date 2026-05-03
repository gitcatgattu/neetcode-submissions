class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap=defaultdict(int)

        for i in range(len(nums)):
            n=nums[i]
            rem=target-n
            if rem in hashMap:
                return [hashMap[rem],i]
            hashMap[n]=i
        