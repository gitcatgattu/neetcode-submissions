class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp=defaultdict(int)

        dp[0]=1
        for i in range(len(nums)):
            dp_next=defaultdict(int)
            for idx,ways in dp.items():
                dp_next[idx+nums[i]]+=ways
                dp_next[idx-nums[i]]+=ways
            dp=dp_next
        return dp[target]
