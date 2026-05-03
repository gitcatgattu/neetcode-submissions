class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        n=len(piles)
        if n>h:
            return False
        l,r=1,max(piles)
        ans=r
        def ispossible(piles,rate):
            eaten=0
            time_taken=0
            for i in piles:
                time_taken+=math.ceil(i/rate)
                eaten+=1
            return time_taken<=h and eaten==n

                






        while l<=r:
            mid=(l+r)//2
            if ispossible(piles,mid):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans
            
                