class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        cords=[(p[0]**2+p[1]**2,p) for p in points]
        heapq.heapify(cords)
        res=[]
        for _ in range(k):
            point=heapq.heappop(cords)
            res.append(point[1])
        return res