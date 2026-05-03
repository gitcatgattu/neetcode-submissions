class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res=[]
        preMap={i:[] for i in range(numCourses)}
        visit=set()
        for cur,pre in prerequisites:
            preMap[cur].append(pre)
        
        def dfs(crs):
            if crs in visit:
                return False
            if preMap[crs]==[]:
                if crs not in res:
                    res.append(crs)
                return True

                        
            
            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            if crs not in res:
                res.append(crs)
            return True





        for i in range(numCourses):
            if not dfs(i):
                return []
        return res