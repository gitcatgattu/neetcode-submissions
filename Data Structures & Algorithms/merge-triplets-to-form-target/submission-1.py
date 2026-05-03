class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a=[False]*3
        for t in triplets:
            flag=True
            for i in range(3):
                if target[i]<t[i]:
                    flag=False
            for i in range(3):
                if flag and not a[i] and target[i]==t[i]:
                    a[i]=True
        print(a)
        return all(a)
