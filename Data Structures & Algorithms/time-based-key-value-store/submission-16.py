class TimeMap:

    def __init__(self):
        self.store=defaultdict(lambda:{"times":[],"vals":[]})
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key]["times"].append(timestamp)
        self.store[key]["vals"].append(value)


    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.store:
            return ''
        
        times,vals=self.store[key]["times"],self.store[key]["vals"]

        l,r=0,len(times)
        while l<r:
            mid=(l+r)//2
            if times[mid]<=timestamp:
                l=mid+1
            else:
                r=mid
        
        idx=l

        if idx==0:
            return ""
        return vals[idx-1]