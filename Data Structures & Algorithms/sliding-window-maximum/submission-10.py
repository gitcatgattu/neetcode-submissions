class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l,res=0,[]
        for r in range(k,len(nums)+1):
            cur=float('-inf')
            for j in range(l,r):
                cur=max(cur,nums[j])
            res.append(cur)

            

            l+=1    
        return res