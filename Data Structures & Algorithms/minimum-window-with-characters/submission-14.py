class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return t
        wcount,tcount=defaultdict(int),defaultdict(int)
        for i in t:
            #scount[s[i]]+=1
            tcount[i]+=1
        have,need=0,len(tcount)
        l=0
        res=[]
        reslen=float('inf')
        for r in range(len(s)):
            
            c=s[r]
            wcount[c]+=1
            if c in tcount and wcount[c]==tcount[c]:
                have+=1
           


            while have==need:
                if reslen>(r-l+1):
                    reslen=r-l+1
                    res=[l,r]
                wcount[s[l]]-=1
                if wcount[s[l]]<tcount[s[l]]:
                    have-=1
                l+=1
                
                
               
                

        if not res:
            return ""
        start,end=res[0],res[1]
        return s[start:end+1]

