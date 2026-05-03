import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums=nums
        self.k=k
        heapq.heapify(self.nums)


    def add(self, val: int) -> int:
        heapq.heappush(self.nums,val)
        res=0
        res=heapq.nlargest(self.k,self.nums)
        return res[-1]

