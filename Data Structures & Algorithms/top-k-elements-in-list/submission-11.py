class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=[[] for _ in range(len(nums)+1)]
        for num,count in Counter(nums).items():
            freq[count].append(num)
        res=[]
        for i in range(len(nums),0,-1):
            while k>0 and freq[i]:
                res.append(freq[i].pop())
                k-=1
        return res