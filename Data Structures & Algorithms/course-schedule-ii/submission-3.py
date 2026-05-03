class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res=[]
        prereq={i:[] for i in range(numCourses)}
        for cur,pre in prerequisites:
            prereq[cur].append(pre)
        

        visit,cycle=set(),set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res 






            
                