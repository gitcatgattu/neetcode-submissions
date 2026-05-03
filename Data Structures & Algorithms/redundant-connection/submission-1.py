class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        parent=[i for i in range(n+1)]
        rank=[1]*(n+1)
        def findParent(n):
            if parent[n]==n:
                return n
            return findParent(parent[n])
        def union(n1,n2):
            p1,p2=findParent(n1),findParent(n2)
            if p1==p2:
                return False#same component ->cycle
            if rank[p1]>=rank[p2]:
                parent[p2]=p1
                rank[p1]+=rank[p2]
            else:
                parent[p1]=p2
                rank[p2]+=rank[p1]
            return True #union done->made their parents same
        #returning first edge that makes a cycle 
        for u,v in edges:
            if not union(u,v):
                return [u,v]
        