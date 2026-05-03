class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        cache={}
        def dfs(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i>=len(s):
                return 1 if j>=len(t) else 0
            if j<len(t) and s[i]==t[j]:
                cache[(i,j)]= dfs(i+1,j+1)+dfs(i+1,j)

            else:
                cache[(i,j)]= dfs(i+1,j)
            return cache[(i,j)]
        return dfs(0,0)
