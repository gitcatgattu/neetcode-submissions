class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp=[defaultdict(int) for i in range(len(nums)+1)]

        dp[0][0]=1
        for i in range(len(nums)):
            for idx,ways in dp[i].items():
                dp[i+1][idx+nums[i]]+=ways
                dp[i+1][idx-nums[i]]+=ways
        return dp[len(nums)][target]
