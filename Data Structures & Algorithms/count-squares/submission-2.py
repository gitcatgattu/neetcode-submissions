class CountSquares:

    def __init__(self):
        self.points=defaultdict(int)
        self.pts=[]
    def add(self, point: List[int]) -> None:
        x,y=point
        self.points[(x,y)]+=1
        self.pts.append(point)
    def count(self, point: List[int]) -> int:
        x,y=point
        res=0
        for dx,dy in self.pts:
            if (abs(x-dx)!=abs(y-dy)) or x==dx or y==dy:
                continue
            # l=(dx,y)
            # r=(x,dy)
            # count=self.points[(dx,dy)]

            # if l in self.points and r in self.points:
            #     count*=self.points[l]
            #     count*=self.points[r]
            #     res+=count
            res+=self.points[(dx,y)]*self.points[(x,dy)]
        return res