class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
       
        intervals.sort()
        n=len(intervals)
        res=[]
        i=0
        while i<n:

            start=intervals[i][0]
            while i+1<n and intervals[i][1]>=intervals[i+1][0]:
                i+=1
                intervals[i][1]=max(intervals[i][1],intervals[i-1][1])
            end=intervals[i][1]
            res.append([start,end])

            i+=1
        return res

            