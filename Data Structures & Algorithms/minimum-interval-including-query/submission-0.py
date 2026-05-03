class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n=len(intervals)
        intervals.sort()
        output=[]
        for q in queries:
            op=float('inf')
            
            for start,end in intervals:
                if start<=q<=end:
                    op=min(op,end-start+1)
                elif start>q:
                    break
            if op==float("inf"):
                op=-1
            output.append(op)
        return output

            