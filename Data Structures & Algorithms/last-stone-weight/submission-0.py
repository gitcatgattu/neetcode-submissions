import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-i for i in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            a=-heapq.heappop(stones)
            b=-heapq.heappop(stones)
            if a>b:
                heapq.heappush(stones,b-a)
            

        if not stones:
            return 0
        return -stones[0]