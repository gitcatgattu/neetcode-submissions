class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        countidx=defaultdict(list)
        for i in range(len(s)):
            if not countidx[s[i]]:
                countidx[s[i]].extend([0,i])
            else: 
                countidx[s[i]][0]+=1
                countidx[s[i]][1]=i
        res=[]
        i=0
        while i<len(s):
            j=i
            l=countidx[s[i]][1]
            while i<=l:
                l=max(countidx[s[i]][1],l)
                i+=1
            res.append(l+1-j)
        return res



