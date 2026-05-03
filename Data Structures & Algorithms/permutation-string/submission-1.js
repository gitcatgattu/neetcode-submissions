class Solution {
    /**
     * @param {string} s1
     * @param {string} s2
     * @return {boolean}
     */
    checkInclusion(s1, s2) {
        if(s1.length>s2.length) return false
        if(s1==s2) return true
        let a=Array(26).fill(0)
        let b=Array(26).fill(0)

        for(let i=0;i<s1.length;i++){
            a[s1[i].charCodeAt(0)-"a".charCodeAt(0)]+=1
            b[s2[i].charCodeAt(0)-"a".charCodeAt(0)]+=1

        }
        if(a.join("")==b.join("")) return true




        let l=0,r=s1.length-1
        while(r<s2.length){
        if(a.join("")==b.join("")) return true

            b[s2[l].charCodeAt(0)-"a".charCodeAt(0)]-=1
            l++
            r++
            if(r<s2.length) b[s2[r].charCodeAt(0)-"a".charCodeAt(0)]+=1

        }








              
        return false
    }
}
