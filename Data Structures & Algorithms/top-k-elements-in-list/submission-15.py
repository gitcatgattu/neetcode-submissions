import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=defaultdict(list)
        for num,freq in Counter(nums).items():
            count[freq].append(num)
        res=[]
        for i in range(len(nums),0,-1):
            for n in count[i]:
                res.append(n)
                if len(res)==k:
                    return res        


