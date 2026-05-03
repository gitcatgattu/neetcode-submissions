class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
       


        adjLst={i:[] for i in range(n)}
        for u,v in edges:
            adjLst[u].append(v)
            adjLst[v].append(u)
        visit=set()
        cycle=set()
        
        def dfs(node,prev):
            # if (node in cycle and node!=prev) or adjLst[node]==[]:#instead of writeing an exit fro recursion do not enter the dfs at all for the particular node
            #we dont need to do dfs on each node any one is enough
            if node in cycle:
                return False
            cycle.add(node)
            for nei in adjLst[node]:
                if nei==prev:
                    continue
                if not dfs(nei,node):
                    return False
            cycle.remove(node)
            return True
        
        return dfs(0,-1)
        # for node in range(n):
        #     if not dfs(node,-1):
        #         return False
        # if len(visit)!=n:
        #     return False
        # return True           