import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=defaultdict(list)
        for num,freq in Counter(nums).items():
            count[freq].append(num)
        i=len(nums)
        res=[]
        j=0
        while j<k:
            while count[i]:
                res.append(count[i].pop()) 
                j+=1
            i-=1
        return res


