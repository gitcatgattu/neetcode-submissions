import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=defaultdict(list)
        for num,freq in Counter(nums).items():
            count[freq].append(num)
        i=len(nums)
        res=[]
        size=0
        while size<k:
            while size<k and count[i]:
                res.append(count[i].pop())
                size+=1
            i-=1
        return res


