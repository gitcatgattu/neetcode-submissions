"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        res=[]
        for i in intervals:
            res.append([i.start,i.end])
        res.sort()
        if len(res)==0:
            return True
        prevEnd=res[0][1]

        for start,end in res[1:]:
            if prevEnd>start:
                return False
            else:
                prevEnd=end
        return True