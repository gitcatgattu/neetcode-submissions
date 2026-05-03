class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
     let ans=0
     for(let r=0;r<s.length;r++){
        let count=new Map()
        let maxf=0
        for(let j=r;j<s.length;j++){
            count.set(s[j],(count.get(s[j])||0)+1)
            maxf=Math.max(maxf,count.get(s[j]))
            if((j-r+1)-maxf<=k){
                ans=Math.max(ans,j-r+1)
            }

        }
     }
        return ans
    }
}
