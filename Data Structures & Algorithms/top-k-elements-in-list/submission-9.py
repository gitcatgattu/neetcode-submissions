class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=[[] for i in range(len(nums)+1)]
        count=Counter(nums)
        for key,val in count.items():
            freq[val].append(key)
        res=[]
        for i in range(len(nums),0,-1):
            while k>0 and freq[i]:
                res.append(freq[i].pop())
                k-=1
        return res
