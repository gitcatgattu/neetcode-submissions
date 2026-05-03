class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        if(s.length==0) return 0
        let l=0,r=1,ans=0,map={}
        while(r<s.length){
            while((s[l]==s[r]||s[r-1]==s[r])&&l<r){
                l+=1
            }

            ans=Math.max(r-l,ans)

            r+=1
            let i=l
            while(i<r){
                if(s[i]==s[r]){
                    l=i
                }
                i++
            }






        }
        return ans+1
        
    }
}
