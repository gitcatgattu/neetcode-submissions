class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
        if(piles.length===h)return Math.max(...piles)

        let l=1,r=Math.max(...piles)
        let ans=r
        while(l<=r){
            const mid=Math.floor((l+r)/2)
            let sum =0
            for(let b of piles){
                sum+=Math.ceil(b/mid)
            }
            
            if(sum<=h){
                ans=Math.min(ans,mid)
                r=mid-1
            }
            else{
                l=mid+1
mid
            }
        }





        return ans
    }
}
