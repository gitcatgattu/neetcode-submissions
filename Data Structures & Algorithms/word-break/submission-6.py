class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache={len(s):True}
        def dfs(i):
            if i in cache:
                return cache[i]
            
            for word in wordDict:
                if s[i:].startswith(word):
                    if dfs(i+len(word)):
                        cache[i]=True
                        return True
            cache[i]=False
            return False
       
      
        return dfs(0)
      
      
      
      
      
      
      
      
      
      
        # dp=[False]*(len(s)+1)
        # dp[len(s)]=True
        # for i in range(len(s)-1,-1,-1):
        #     for w in wordDict:
        #         if s[i:].startswith(w) and dp[i+len(w)]:
        #             dp[i]=True
        # return dp[0]



        #dp={len(s):1}
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

