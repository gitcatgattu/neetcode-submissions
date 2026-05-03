class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        let l=0,ans=0,charSet=new Set()
        for(let r=0;r<s.length;r++){
            while(charSet.has(s[r]) ){
                charSet.delete(s[l])
                l+=1

            }
            charSet.add(s[r])
            ans=Math.max(ans,r-l+1)

        }
        return ans
        
    }
}
