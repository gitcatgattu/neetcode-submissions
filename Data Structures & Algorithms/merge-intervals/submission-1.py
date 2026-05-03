class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        

        intervals.sort()
        res=[intervals[0]]
        i=1
        while i<len(intervals):
            if res[-1][1]<intervals[i][0]:
                res.append(intervals[i])
            else:
                while i<len(intervals) and res[-1][1]>=intervals[i][0]:
                    res[-1][1]=max(intervals[i][1],res[-1][1])
                    i+=1
                continue
                


            i+=1
        return res