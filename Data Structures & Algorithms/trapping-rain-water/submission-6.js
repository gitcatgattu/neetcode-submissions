class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        let maxLeft=[],maxRight=[],minLR=[],a=0
        
        for(let h of height){
            maxLeft.push(a)
            if(h>a)a=h
        }
        a=0
        for(let i=height.length;i>=0;i--){
            maxRight.unshift(a)
            if(height[i]>a)a=height[i]
        }
        for(let i=0;i<height.length;i++){
            minLR.push(Math.min(maxLeft[i],maxRight[i]))
        }
        let sum=0
        for(let i=0;i<height.length;i++){
            if(minLR[i]-height[i]>0)
            sum+=minLR[i]-height[i]

        }
        return sum
    }
}
