class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures) {
        let res=Array(temperatures.length).fill(0)
        let stack=[]
        for(let i=0;i<temperatures.length;i++){
            const t=temperatures[i]
            
            while(stack.length>0 && t>stack[stack.length-1][1]){
                const [idx,temp]=stack.pop()
                res[idx]=i-idx
            }
            stack.push([i,t])

        }
        return res
    }
}
