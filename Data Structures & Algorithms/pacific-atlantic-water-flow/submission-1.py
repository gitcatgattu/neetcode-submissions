class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS,COLS=len(heights),len(heights[0])
            
        visitpacific=set()
        visitatlantic=set()
        pq=deque()
        aq=deque()
        def addPac(r,c,h):
            if r<0 or c<0 or r>=ROWS or c>=COLS or heights[r][c]<h or (r,c) in visitpacific:
                return
            visitpacific.add((r,c))
            pq.append([r,c])
        def addAtl(r,c,h):
            if r<0 or c<0 or r>=ROWS or c>=COLS or heights[r][c]<h or (r,c) in visitatlantic:
                return
            visitatlantic.add((r,c))
            aq.append([r,c])
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if r==0 or c==0:
                    pq.append([r,c])
                    visitpacific.add((r,c))
                if r==ROWS-1 or c==COLS-1:
                    aq.append([r,c])
                    visitatlantic.add((r,c))

        while len(pq)>0:
            for i in range(len(pq)):
                r,c=pq.popleft()
                h=heights[r][c]
                addPac(r+1,c,h)
                addPac(r,c+1,h)
                addPac(r-1,c,h)
                addPac(r,c-1,h)
        while len(aq)>0:
            for i in range(len(aq)):
                r,c=aq.popleft()
                h=heights[r][c]
                addAtl(r+1,c,h)
                addAtl(r,c+1,h)
                addAtl(r-1,c,h)
                addAtl(r,c-1,h)
        
        return list(visitatlantic.intersection(visitpacific))
        


