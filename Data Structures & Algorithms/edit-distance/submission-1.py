class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        cache={}
        def dfs(i,j):
            if i>=m or j>=n:
                return max(m-i,n-j)
            if word1[i]==word2[j]:
                
                cache[(i,j)]= dfs(i+1,j+1)
                return cache[(i,j)]
            cache[(i,j)]= min(dfs(i+1,j),dfs(i,j+1),dfs(i+1,j+1))+1
            return cache[(i,j)]
        return dfs(0,0)