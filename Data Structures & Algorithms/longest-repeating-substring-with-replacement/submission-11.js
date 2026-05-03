class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
     let l=0,maxfreq=0,ans=0
     const count={}
     for(let r=0;r<s.length;r++){
        count[s[r]]=(count[s[r]]||0)+1
       maxfreq=Math.max(maxfreq,count[s[r]])
        while((r-l+1)-maxfreq>k){
            count[s[l]]--
            l++
        }
        ans=Math.max(ans,r-l+1)
     }
     return ans

    }
}
