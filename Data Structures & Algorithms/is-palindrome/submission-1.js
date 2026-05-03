class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        s=s.replace(/[^a-zA-Z0-9]/g,"")
        let st=""
        for(let i=s.length-1;i>=0;i--){
            if(s[i]!=" ")
            st+=s[i].toLowerCase()
        }
        console.log(st)
        console.log(s.toLocaleLowerCase().replace(/ /g,""))
        return st===s.toLocaleLowerCase()
    }
}
