class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        

        adjLst={i:[] for i in range(n)}
        for u,v in edges:
            adjLst[u].append(v)
            adjLst[v].append(u)



















        visited=set()

        self.ans=0
        def dfs(i,parent):
            if i in visited:
                return
            visited.add(i)
            for nei in adjLst[i]:
                dfs(nei,i)
            if i==parent:
                self.ans+=1
            
            
        for node in range(n):
            if node not in visited:
                dfs(node,node)
        return self.ans

            