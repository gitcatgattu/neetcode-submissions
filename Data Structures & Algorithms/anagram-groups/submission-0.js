class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */

    groupAnagrams(strs) {
        const ans=[]
        const n=strs.length
        const visited=Array(n).fill(false)
        for(let i=0;i<n;i++){

        let sublist=[]
        if(!visited[i]){
        for(let j=i+1;j<n;j++){

            let s=strs[i]
            let t=strs[j]
            if(s.length===t.length){

                let flag=true

 const alph=Array(26).fill(0)
        for(let char of s){
            alph[char.charCodeAt(0)-'a'.charCodeAt(0)]+=1

        }
        for(let char of t){
            let index=char.charCodeAt(0)-'a'.charCodeAt(0)
            alph[index]-=1
            if(alph[index]<0) flag=false

        }

                if(flag){
        visited[j]=true

                sublist.push(strs[j])

                }
            }
            
        }
        visited[i]=true

        sublist.push(strs[i])
        ans.push(sublist)}
       }
       return ans
    }
}
