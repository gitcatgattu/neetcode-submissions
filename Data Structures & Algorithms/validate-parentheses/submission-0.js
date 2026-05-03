class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        let stack=[]
        for(let br of s){
            if(br=="("||br=="{"||br=="["){
                stack.push(br)
            }
            else if(br==")"&&stack[stack.length-1]=="("){
                stack.pop()
            }
            else if(br=="}"&&stack[stack.length-1]=="{"){
                stack.pop()
            }
            else if(br==="]"&&stack[stack.length-1]=="["){
                stack.pop()
            }
            else{
                return false
            }
        }
    return stack.length==0
    }
}
