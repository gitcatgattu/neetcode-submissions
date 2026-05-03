class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False]*(len(s)+1)
        dp[len(s)]=True
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if s[i:].startswith(w) and dp[i+len(w)]:
                    dp[i]=True
        return dp[0]




        # def dfs(i):
        #     if i in dp:
        #         return dp[i]
        #     for w in wordDict:
        #         if s[i:].startswith(w) and dfs(i+len(w)):
        #                 dp[i]=True
        #                 return True
        #     dp[i]=False
        #     return False
        # return dfs(0)