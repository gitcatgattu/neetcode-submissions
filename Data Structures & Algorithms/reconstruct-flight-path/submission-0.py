class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList=collections.defaultdict(list)
        tickets.sort()
        for s,d in tickets:
            adjList[s].append(d)
        
        res=["JFK"]
        def dfs(n):
            
            if len(res)==len(tickets)+1:
                return True
            if n not in adjList:
                return False
            

            temp=list(adjList[n])
            for i,dst in enumerate(temp):
                res.append(dst)
                adjList[n].pop(i)
                if dfs(dst):
                    return True
                adjList[n].insert(i,dst)
                res.pop()
            return False
        
        dfs("JFK")
        return res