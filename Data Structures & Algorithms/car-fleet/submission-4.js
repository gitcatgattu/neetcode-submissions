class Solution {
    /**
     * @param {number} target
     * @param {number[]} position
     * @param {number[]} speed
     * @return {number}
     */
    carFleet(target, position, speed) {
        let comb=[]
        for(let i=0;i<speed.length;i++){
            let c=[position[i],speed[i]]
            comb.push(c)
        }
        comb=comb.sort((a,b)=>a[0]-b[0])
        let stack=[]
        for(let i=comb.length-1;i>=0;i--){
            stack.push((target-comb[i][0])/comb[i][1])
            
            if(stack.length>=2 && stack[stack.length-1]<=stack[stack.length-2]){
                
                stack.pop()}
        }
        return stack.length

    }
}
