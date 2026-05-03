class Solution {
    /**
     * @param {number} n
     * @return {string[]}
     */
    generateParenthesis(n) {
        let stack=[]
        let res=[]
        function backtrack(open,close){
            if(open==close&&close==n){
                res.push(stack.join(""))
                return
            }
            if(open<n){
                stack.push("(")
                backtrack(open+1,close)
                stack.pop()
            }
            if(open>close){
                stack.push(")")
                backtrack(open,close+1)
                stack.pop()


            }
        }
        backtrack(0,0)
        return res


    }
}
