class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        
        def dfs(i,j):
            if i>=m or j>=n:
                return max(m-i,n-j)
            
            if word1[i]==word2[j]:
                return dfs(i+1,j+1)
            return min(dfs(i+1,j),dfs(i,j+1),dfs(i+1,j+1))+1
        return dfs(0,0)