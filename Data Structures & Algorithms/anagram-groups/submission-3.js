class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */

    groupAnagrams(strs) {
       let map={}
       for(let str of strs){
            let count=Array(26).fill(0)
            for(let char of str){
                count[char.charCodeAt(0)-'a'.charCodeAt(0)]+=1
            }
            count=count.join('#')
            console.log(count)
            if(map[count]===undefined) map[count]=[str]
            else map[count].push(str)
       }
       return Object.values(map)
    }
}
