class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
    if (s.length !== t.length) {
        return false;
    }
    const freq=Array(26).fill(0)
    for(let char of s){
        freq[char.charCodeAt(0)-'a'.charCodeAt(0)]+=1
    }
    for(let char of t){
        const index=char.charCodeAt(0)-'a'.charCodeAt(0)
        freq[index]-=1
        if(freq[index]<0){
            return false
        }
    }
    return true
}
}
