class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
        let stack=[]
        console.log("6/132 is",Math.floor(6/-132))
        for(let s of tokens){
            if(s==="+"){
                let b=stack.pop()
                let a=stack.pop()
                stack.push(a+b)
console.log(a+b)

            }
            else if(s==="-"){
                 let b=stack.pop()
                let a=stack.pop()
                stack.push(a-b)
console.log(a-b)


            }
            else if(s==="*"){
                 let b=stack.pop()
                let a=stack.pop()
console.log(a*b)
                stack.push(a*b)

            }
            else if(s==="/"){
                 let b=stack.pop()
                let a=stack.pop()
                console.log(Math.floor(a/b))
                stack.push(Math.floor(a/b)<0?Math.ceil(a/b):Math.floor(a/b))

            }else{
                stack.push(Number(s))
                console.log(Number(s))
            }
        }
        if(stack.length==1) return stack.pop()
    }
}
