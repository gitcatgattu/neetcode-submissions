class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        if(strs.length==0) return ""
        let res=""
       for(let st of strs){
        res+=st.length+"#"+st
       }
       return res
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let i=0,res=[]
        while(i<str.length){
            let j=i
            while(str[j]!=="#"){
                j+=1
            }
            let range=parseInt(str.substring(i,j))
            i=j+1
            j=i+range

            let word=str.substring(i,j)
            res.push(word)
            i=j

        }
return res






    }
}
