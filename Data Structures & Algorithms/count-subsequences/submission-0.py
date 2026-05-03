class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        

        def dfs(i,j):
            if i>=len(s):
                return 1 if j>=len(t) else 0
            if j<len(t) and s[i]==t[j]:
                return dfs(i+1,j+1)+dfs(i+1,j)
            else:
                return dfs(i+1,j)
        return dfs(0,0)
