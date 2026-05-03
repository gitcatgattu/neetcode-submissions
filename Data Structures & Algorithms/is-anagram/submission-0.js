class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if(s.length!==t.length) return false;
        let hash1={}
        let hash2={}
        for(let i=0;i<s.length;i++){
            if(hash1[s[i]]) hash1[s[i]]+=1
            else hash1[s[i]]=1
            if(hash2[t[i]]) hash2[t[i]]+=1
            else hash2[t[i]]=1
        }
        for(let i=0;i<s.length;i++){
            if(hash1[s[i]]!==hash2[s[i]]){
                return false
            }
        }
        console.log(hash1,hash2)
        return true
        
        
    }
}
