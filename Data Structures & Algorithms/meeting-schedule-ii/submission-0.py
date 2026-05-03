"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        slots=[]
        for i in intervals:
            slots.append([i.start,"s"])
            slots.append([i.end,"e"])

        slots.sort()
        res=0
        rooms=0
        for i in slots:
            if i[1]=="s":
                rooms+=1
            else:
                rooms-=1
            res=max(res,rooms)
        return res
