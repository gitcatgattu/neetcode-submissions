class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        d=collections.defaultdict(list)

        for i,c in count.items():
            d[c].append(i)

        res=[]
        print(d)
        i=0
        while len(res)<k and i<=len(nums): 
            for n in d[len(nums)-i]:
                if len(res)<k:
                    res.append(n)
                else:
                    break
            i+=1
        return res
